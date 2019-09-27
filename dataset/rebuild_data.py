import json

'''
This script is use to merge the two json dataset 
and to remove severals useless information in the dataset. 
'''

def transformDataset1FromJson(json_path, final_data):
    '''transform the input json file
   
    json_path -- json path from the first dataset
    final_data -- final buffer for the json file
    '''
    with open(json_path) as json_file:
        dataset = json.load(json_file)
        for line in dataset :
            del line['source']
            del line['cashtag']
            del line['id']
            
            line['title'] = ''

            for span in line['spans']:
                line['title'] += span + ' '
            del line['spans']

            line['sentiment'] = line['sentiment score']
            del line['sentiment score']
            final_data.append(line)
    return dataset

def transformDataset2FromJson(json_path, final_data):
    '''transform the input json file
   
    json_path -- json path from the second dataset
    final_data -- final buffer for the json file
    '''
    with open(json_path) as json_file:
        dataset = json.load(json_file)
        for line in dataset:
            del line['id']
            del line['company']
            final_data.append(line)
    return json.dumps(dataset)

if __name__ == "__main__":
    final_data = []
    dataset1_train = transformDataset1FromJson('dataset1/Microblog_Trainingdata.json', final_data)
    dataset1_trial = transformDataset1FromJson('dataset1/Microblog_Trialdata.json', final_data)

    dataset2_train = transformDataset2FromJson('dataset2/Headline_Trainingdata.json', final_data)
    dataset2_trial = transformDataset2FromJson('dataset2/Headline_Trialdata.json', final_data)
    
    with open('financialData.json', 'w') as f:
        json.dump(final_data, f)