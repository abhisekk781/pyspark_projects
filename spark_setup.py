def setup():
    import findspark
    import os
    spark_location='/Users/abhisekkumar/spark3/' # Set your own
    java8_location='/Library/Java/JavaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home'
    # Set your own
    os.environ['JAVA_HOME'] = java8_location
    findspark.init(spark_home=spark_location)
    
    
if __name__ == '__main__':
    setup()
    