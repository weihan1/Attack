import torch
from dataset import *
from transformers import BertForSequenceClassification, BertTokenizer, pipeline
from textattack import Attacker
from textattack.attack_recipes.bae_garg_2019 import BAEGarg2019
from textattack.attack_recipes.bert_attack_li_2020 import BERTAttackLi2020          
from textattack.datasets import HuggingFaceDataset
from textattack.models.wrappers import ModelWrapper
from api_dataset import API
import numpy as np
import logging
import textattack
logging.getLogger("transformers").setLevel(logging.ERROR)
from textattack.constraints.pre_transformation import RepeatModification, StopwordModification
from textattack.constraints.semantics import WordEmbeddingDistance
from textattack import Attack
from textattack.datasets import Dataset
import transformers
if __name__ == "__main__":
    
    model = BertForSequenceClassification.from_pretrained('bert-base-uncased')
    model.load_state_dict(torch.load("models/best_model.pt"))
    model.eval()
    # print(model)
    
# Configure the TextAttack attack recipe
    
    dataset2 = API().convert_text_to_lst("new_train_dataset_api.txt")
    dataset_transformed = [(text, 1) for text in dataset2]
    # print(dataset_transformed[0])
    tokenizer = transformers.AutoTokenizer.from_pretrained("textattack/bert-base-uncased-imdb")
    model_wrapper = textattack.models.wrappers.HuggingFaceModelWrapper(model, tokenizer)
    # goal_function = textattack.goal_functions.UntargetedClassification(model_wrapper)
    # constraints = [RepeatModification(),
    #                  StopwordModification(),
    #                     WordEmbeddingDistance(min_cos_sim=0.8)]
    # transformation = textattack.transformations.WordSwapEmbedding(max_candidates=50)
    # search_method = textattack.search_methods.GreedyWordSwapWIR(wir_method="delete")
    attack_args = textattack.AttackArgs(
        num_examples=20,
        log_to_csv = "log.csv",
        checkpoint_interval=5,
        checkpoint_dir="checkpoints/",
        disable_stdout=False,
    )
    attack = BERTAttackLi2020.build(model_wrapper)
    dataset = Dataset(dataset_transformed)
    
    attacker = textattack.Attacker(attack, dataset, attack_args)
    print(attacker.attack_dataset())
    
