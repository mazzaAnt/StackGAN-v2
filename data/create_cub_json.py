import os, json

cub, img_id, sentid = {'images': [], 'dataset': 'cub'}, 0, 0

ROOT = '%s/%s' % (os.getcwd(), 'birds/text_c10') 
dirs = os.listdir(ROOT)

for d in dirs: 
     directory = os.path.join(ROOT, d) 
     for f in os.listdir(directory): 
         full_path = os.path.join(directory, f) 
         print (full_path) 
         img_struct = {'imgid': img_id, 'filepath': d, 'filename': '%s.jpg' % f.split('.')[0], 'split': 'train', 'cocoid': -1, 'sentences': [],
  'sentids': []} 
         file =  open(full_path, 'r') 
         sentids = [] 
         for line in file: 
             #print (line) 
             sent_struct = {} 
             sent_struct['raw'] = line 
             sent_struct['sentid'] = sentid 
             img_struct['sentids'].append(sentid) 
             sentid += 1 
             sent_struct['tokens'] = line.split(' ') 
             img_struct['sentences'].append(sent_struct) 
         cub['images'].append(img_struct) 
         img_id += 1 
         file.close() 
         
         
with open('cub.json', 'w') as out:
	json.dump(cub, out)	