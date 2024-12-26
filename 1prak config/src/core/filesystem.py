import os
import zipfile

class VirtualFileSystem:
    def __init__(self, zip_ref):
         self.zip_ref = zip_ref
         self.tree = self._build_tree()
         self.current_dir = '/'

    def _build_tree(self):
         tree = {}
         for file_info in self.zip_ref.infolist():
              path = file_info.filename
              if path.endswith('/'):
                # Directory
                if path == '/':
                   tree['/'] = {'files': [], 'dirs': {}}
                else:
                   parts = path.split('/')[:-1] # Ignore the last empty string
                   current = tree
                   for part in parts:
                        if part not in current.get('dirs', {}):
                             current.setdefault('dirs', {})[part] = {'files': [], 'dirs': {}}
                        current = current['dirs'][part]
              else:
                # File
                parts = path.split('/')
                if len(parts) > 1:
                     dir_parts = parts[:-1]
                     current = tree
                     for part in dir_parts:
                          if part not in current.get('dirs', {}):
                             current.setdefault('dirs', {})[part] = {'files': [], 'dirs': {}}
                          current = current['dirs'][part]
                     current.get('files',[]).append(parts[-1])
                else:
                     tree.setdefault('files', []).append(parts[0])
         return tree
    
    def _resolve_path(self, path):
         if path.startswith('/'):
             return path.split('/')[1:]
         else:
             current_path = self.current_dir.split('/')[1:]
             return current_path + path.split('/')

    def _get_node(self, path_parts):
        current = self.tree
        for part in path_parts:
            if part == '' :
                continue
            if not current.get('dirs', {}).get(part):
                 return None
            current = current['dirs'][part]
        return current
   
    def list_dir(self, path='.'):
        path_parts = self._resolve_path(path)
        node = self._get_node(path_parts)

        if not node:
             return None
        
        dirs = node.get('dirs',{}).keys()
        files = node.get('files',[])
        return list(dirs) + list(files)
       
    def change_dir(self, path):
        if path == '..':
             if self.current_dir == '/':
                 return self.current_dir
             else:
                 self.current_dir = '/'.join(self.current_dir.split('/')[:-1]) or '/'
                 return self.current_dir
        
        path_parts = self._resolve_path(path)
        node = self._get_node(path_parts)

        if node is None:
            return None
        
        self.current_dir =  '/' + '/'.join(path_parts) if path_parts else '/'

        return self.current_dir
    
    def get_current_dir(self):
         return self.current_dir
    
    def file_exists(self, path):
        path_parts = self._resolve_path(path)
        node = self._get_node(path_parts[:-1])
        if node and path_parts[-1] in node.get('files', []):
            return True
        return False

    def read_file(self, path):
         try:
              if not self.file_exists(path):
                   return None
              file_name = '/'.join(self._resolve_path(path))
              with self.zip_ref.open(file_name) as file:
                    return file.read().decode('utf-8')
         except Exception as e:
               print(f"Error reading file: {e}")
               return None