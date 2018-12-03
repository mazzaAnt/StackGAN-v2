from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='CUB',
                       karpathy_json_path='./data/cub.json',
                       image_folder='./TEMP_IMAGES/',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder='./code/birds_output/',
                       max_len=50)
