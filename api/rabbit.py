import pika


class Rabbit():
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='launch_files')
        self.channel.queue_declare(queue='processes')

    def send_launch_files(self, data):
        self.channel.basic_publish(exchange='',
                            routing_key='launch_files',
                            body=bytes(data, 'utf-8'))


    def send_procs(self, data):
        self.channel.basic_publish(exchange='',
                            routing_key='processes',
                            body=bytes(data, 'utf-8'))
