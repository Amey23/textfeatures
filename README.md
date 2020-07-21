# **Introduction: textfeatures**
When we handle the text data, we always have concerns about the data features, pre-processing of data and more likely the predictions. To improve our model, it is important to understand the data and find the more interesting features in the data like hashtags, links and many more.

## **What is textfeatures?**

It is a python package which helps you to extract the basic features from the text data such as hashtags, stopwords, numerics which will help you to understand the data and improve your model more effectively.

## **Function structure:**

## function_name(dataframe, ”text_column”, ”new_column”)

**dataframe:- name of dataframe**

**text_column:- name of the column from which features are to be extracted.**

**new_column:- new column derived by feature extraction from text_column.**

# **What will textfeatures serve you?**

**1. word_count():-** give the total words count present in text data.

**2. char_count():-** give the characters count.

**3. avg_word_length():-** give the average word length.

**4. stopwords_count()**:- give the stopwords count.

**5. stopwords()**:- extract the stopwords from the text data.

**6. hashtags_count():-** give the hashtags count.

**7. hashtags():-** extract the hashtags from text data.

**8. links_count():-** give the embedded links count from text data.

**9. links():-** extract the links from the text data.

**10. numeric_count():-** give the numeric digits count.

**11. user_mentions_count():-** give the user mentions count from text data.

**12. user_mentions():-** extract the user mentions from text data.

**13. clean():-** give the pre-processed data after removal for unnecessary material in text data. 
