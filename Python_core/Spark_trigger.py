import pyspark

sc = pyspark.SparkContext()
txt =  sc.textFile('file:///C:/Users/DELL/OneDrive/Documents/Batch15/Batch_15_Guest_Section_Develop_life_cycle.txt')
print(txt.count())


