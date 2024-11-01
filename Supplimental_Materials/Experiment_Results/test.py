import os
import pickle


target_path='./framework_results.pkl'

with open(target_path, 'rb') as f:#input,bug type,params
    target_dict = pickle.load(f)

for key in target_dict.keys():
    tmp_dict=target_dict[key]
    save_path=f'./framework-{key}.pkl'
    with open(save_path, 'wb') as f:
        pickle.dump(tmp_dict, f)