from kafka import KafkaProducer
from time import sleep
from json import dumps

# Create a Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['13.234.37.35:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)
print("connected")
# Send 10 messages
for i in range(10):
    message = {'number': i}
    producer.send('test-topic', value=message)
    print(f'Sent: {message}')

# Close the producer
producer.flush()
