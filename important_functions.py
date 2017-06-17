# To display one image with the label from the dataset
def display_im(X,y):
    index=random.randint(0,len(X))
    image=X[index].squeeze()
    plt.figure(figsize=(4,4))
    plt.imshow(image)
    print('Output Label for the input is :', y[index])
    
    
    

def dataset_download(dataset_folder,filename,download_url):
    
    # To download dataset (filename) in dataset_folder from download_url and if downloaded already to verify if they are present
    # dataset_folder: folder containing all datasets
    # filename: name of the dataset to be downloaded along with extension
    # download_url: url to be used to download the dataset
    
    
    from urllib.request import urlretrieve
    from os.path import isfile, isdir
    from tqdm import tqdm
    import os
    
    class DLProgress(tqdm):
            last_block = 0

            def hook(self, block_num=1, block_size=1, total_size=None):
                self.total = total_size
                self.update((block_num - self.last_block) * block_size)
                self.last_block = block_num
                
    if os.path.exists(dataset_folder):
        print('Datasets folder exists')
    else:
        os.makedirs(dataset_folder)
          
    if os.path.exists(dataset_folder+'/'+filename):
        print('%s dataset present'%(filename))
    else:        
        with DLProgress(unit='B', unit_scale=True, miniters=1, desc=filename) as pbar:
            urlretrieve(url, folder+'/'+filename , pbar.hook)
