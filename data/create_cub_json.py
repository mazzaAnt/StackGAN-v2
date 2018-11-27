import os, json, pickle

train_filenames_pickle = 'birds/train/filenames.pickle'
test_filenames_pickle = 'birds/test/filenames.pickle'

with open(train_filenames_pickle, 'rb') as f:
    train_filenames = pickle.load(f)

print (train_filenames)
with open(test_filenames_pickle, 'rb') as f:
    test_filenames = pickle.load(f)

cub, img_id, sentid = {'images': [], 'dataset': 'cub'}, 0, 0

ROOT = '%s/%s' % (os.getcwd(), 'birds/text_c10') 
dirs = os.listdir(ROOT)

for d in dirs: 
     directory = os.path.join(ROOT, d) 
     for f in os.listdir(directory): 
         full_path = os.path.join(directory, f) 
         print (full_path) 
         fileroot = f.split('.')[0]
         if '%s/%s' % (d, fileroot) in train_filenames:
             split = 'train'
         elif '%s/%s' % (d, fileroot) in test_filenames:
             split = 'test'
         else:
             raise Exception("filename %s is not in any list!" % fileroot)
         img_struct = {'imgid': img_id, 'filepath': d, 'filename': '%s.jpg' % fileroot, 'split': split, 'cocoid': -1, 'sentences': [],'sentids': []} 
         file =  open(full_path, 'r') 
         sentids = [] 
         for line in file: 
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
