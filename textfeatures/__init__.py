import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop = stopwords.words('english')

def word_count(df,text,name):
    df[name] = df[text].apply(lambda x : len(str(x).split(" ")))
    return df

def char_count(df,text,name):
    df[name] = df[text].str.len() ## this also includes spaces
    return df

def avg_word_length(df,text,name):
  def avg_word(sent):
    words = sent.split()    
    return (sum(len(word) for word in words)/len(words))
  df[name] = df[text].apply(lambda x: avg_word(x))
  return df

def stopwords_count(df,text,name):
    df[name] = df[text].apply(lambda x: len([x for x in x.split() if x in stop]))
    return df

def stopwords(df,text,name):
    df[name] = df[text].apply(lambda x: [x for x in x.split() if x in stop])
    return df

def hashtags_count(df,text,name):
    df[name] = df[text].apply(lambda x: len([x for x in x.split() if x.startswith('#')]))
    return df

def hashtags(df,text,name):
    df[name] = df[text].apply(lambda x: [x for x in x.split() if x.startswith('#')])
    return df

def user_mentions_count(df,text,name):
    df[name] = df[text].apply(lambda x: len([x for x in x.split() if x.startswith('@')]))
    return df

def user_mentions(df,text,name):
    df[name] = df[text].apply(lambda x: [x for x in x.split() if x.startswith('@')])
    return df

def numerics_count(df,text,name):
    df[name] = df[text].apply(lambda x: len([x for x in x.split() if x.isdigit()]))
    return df

def links_count(df,text,name):
    df[name] = df[text].apply(lambda x: len([x for x in x.split() if x.startswith(('httP','HTTPS','https','www','WWW','HTTP','http'))]))
    return df
	
def links(df,text,name):
    df[name] = df[text].apply(lambda x: [x for x in x.split() if x.startswith(('httP','HTTPS','https','www','WWW','HTTP','http'))])
    return df


def clean(df,text,name):
  df[name] = df[text].str.lower()
  df[name] = df[name].str.replace('http\S+|www.\S+', '', case=False)
  df[name] = df[name].str.replace('[^\w\s]','')
  df[name] = df[name].str.replace('\d+', '')
  df[name] = df[name].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
  df[name] = df[name].apply(lambda x: " ".join(x for x in x.split() if len(x)>3))
  return df