API_KEY = 'gz3n1iY9BQLwAW8VvISRNRvkk'
API_SECRET_KEY = '5h2t83uUt6pynCO0qZJaf0Q0HieYkH01fX6yk9tTWrCIAiOVUe'
ACCESS_TOKEN = '1358676935136534529-i2OLlPV9VtHJJD23xJRIaZRj6XFUfO'
ACCESS_TOKEN_SECRET= 'V9FSiWA6ust7Ftgr4mP5tUeUI4l2jht9z0vCMdvDtJ9eV'


#zookeeper-server-start.bat ../../config/zookeeper:properties

#kafka-server-start.bat ../../config/server.properties

## topic 만든거 이름을 twitterdata1으로
#
#kafka-topics.bat --zookeeper localhost:2181 --topic twitterdata1 --create -partitions 1 --replication-factor 1

#kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic twitterdata1 --from-beginning
