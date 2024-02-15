# Model from huggingface
MODEL = "alvarophylipe/portuguese-fake-news-classification"

# Tokenization Parameters
MAX_LEN: int = 512
PADDING: str = 'max_length'
TRUNCATION: bool = True
TENSOR_TYPE: str = 'tf'
ADD_SPECIAL_TOKENS: bool = True
RETURN_TOKEN_TYPE_IDS: bool = True
RETURN_ATTENTION_MASK: bool = True
DO_LOWER_CASE: bool = False