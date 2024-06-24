from operator import truediv


class ReceiverProcess:
    """ Represent the receiver process in the application layer  """
    __buffer = list()

    @staticmethod
    def deliver_data(data):
        """ deliver data from the transport layer RDT receiver to the application layer
        :param data: a character received by the RDT RDT receiver
        :return: no return value
        """
        ReceiverProcess.__buffer.append(data)
        return

    @staticmethod
    def get_buffer():
        """ To get the message the process received over the network
        :return:  a python list of characters represent the incoming message
        """
        return ReceiverProcess.__buffer


class RDTReceiver:
    """" Implement the Reliable Data Transfer Protocol V2.2 Receiver Side """

    def __init__(self):
        self.sequence = '0'

    @staticmethod
    def is_corrupted(packet):
        """ Check if the received packet from sender is corrupted or not
            :param packet: a python dictionary represent a packet received from the sender
            :return: True -> if the reply is corrupted | False ->  if the reply is NOT corrupted
        """
        # TODO provide your own implementation
        "Check sequence number not 1 or 0 and that the data sent is equivalent to the checksum of the packet""CHANGEDDDD"

        if (packet['checksum']!=ord(packet['data']) or (packet['sequence_number'] !='1' and packet['sequence_number'] !='0') ):
            return True
        return False
       

        pass

    @staticmethod
    def is_expected_seq(rcv_pkt, exp_seq):
        """ Check if the received reply from receiver has the expected sequence number
         :param rcv_pkt: a python dictionary represent a packet received by the receiver
         :param exp_seq: the receiver expected sequence number '0' or '1' represented as a character
         :return: True -> if ack in the reply match the   expected sequence number otherwise False
        """
        # TODO provide your own implementation CHANGEEEED
        if (rcv_pkt['sequence_number']==exp_seq):
            return True
        return False    
        
        pass


    @staticmethod
    def make_reply_pkt(seq, checksum):
        """ Create a reply (feedback) packet with to acknowledge the received packet
        :param seq: the sequence number '0' or '1' to be acknowledged
        :param checksum: the checksum of the ack the receiver will send to the sender
        :return:  a python dictionary represent a reply (acknowledgement)  packet
        """
        reply_pck = {
            'ack': seq,
            'checksum': checksum
        }
        return reply_pck

    def rdt_rcv(self, rcv_pkt):
        """  Implement the RDT v2.2 for the receiver
        :param rcv_pkt: a packet delivered by the network layer 'udt_send()' to the receiver
        :return: the reply packet
        """

        # TODO provide your own implementation
        "NOTE:First check if data recieved is corrupted then process the data if corrupted send mesaage indicating that" 
        

        

        print(f'RECIEVER expecting seq_num:',self.sequence)
        if(self.is_corrupted(rcv_pkt) or (self.is_expected_seq(rcv_pkt,self.sequence))==False):#Checks if packet received corrupted or not and the sequenceNO is correct
            print(f'network_layer:corruption occured',rcv_pkt)
            temp='0'
            if(self.sequence=='0'):
                temp='1'
            else:
                temp='0' #Flip sequence number after sending packet if not corrupted
            reply_pkt = RDTReceiver.make_reply_pkt(temp,ord(temp))   
            
            
        else:
            reply_pkt = RDTReceiver.make_reply_pkt(self.sequence,ord(self.sequence))  
            if(self.sequence=='0'):
                self.sequence='1'
            else:
                self.sequence='0' #Flip sequence number after sending packet if not corrupted
            ReceiverProcess.deliver_data(rcv_pkt['data'])#Insert data inside buffer if not corrupted   

        
        
        print(f'RECIEVER reply with:',reply_pkt)
        print(f'SENDER recieved :',reply_pkt)
        return reply_pkt  # deliver the data to the process in the application layer
    
