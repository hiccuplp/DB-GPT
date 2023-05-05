#!/usr/bin/env python3 
# -*- coding:utf-8 -*-

import torch
import os

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODEL_PATH = os.path.join(ROOT_PATH, "models")
VECTORE_PATH = os.path.join(ROOT_PATH, "vector_store")
LOGDIR = os.path.join(ROOT_PATH, "logs")
DATASETS_DIR = os.path.join(ROOT_PATH, "pilot/datasets")

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
LLM_MODEL_CONFIG = {
    "flan-t5-base": os.path.join(MODEL_PATH, "flan-t5-base"),
    "vicuna-13b": os.path.join(MODEL_PATH, "vicuna-13b"),
    "sentence-transforms": os.path.join(MODEL_PATH, "all-MiniLM-L6-v2")
}


LLM_MODEL = "vicuna-13b"
LIMIT_MODEL_CONCURRENCY = 5
MAX_POSITION_EMBEDDINGS = 2048
VICUNA_MODEL_SERVER = "http://192.168.31.114:8000"


# Load model config
ISLOAD_8BIT = True
ISDEBUG = False


DB_SETTINGS = {
    "user": "root",
    "password": "aa123456",
    "host": "localhost",
    "port": 3306
}