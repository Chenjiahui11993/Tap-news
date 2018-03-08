from cloudAMQP_client import CloudAMQPClient

CLOUDAMQP_URL = "amqp://srmxtnxj:piWxfG1kIPdEzjPTNXaP3Bef2vfuqWBD@termite.rmq.cloudamqp.com/srmxtnxj"
TEST_QUEUE_NAME = "test"

def test_basic():
    client = CloudAMQPClient(CLOUDAMQP_URL, TEST_QUEUE_NAME)

    sentMsg = {"test":"test"}
    client.sendMessage(sentMsg)
    receivedMsg = client.getMessage()

    assert sentMsg == receivedMsg
    print("test_basic passed!")

if __name__ == "__main__":
    test_basic()