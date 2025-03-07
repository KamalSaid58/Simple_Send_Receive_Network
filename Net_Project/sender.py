class SenderProcess:
    """ Represent the sender process in the application layer  """

    __buffer = list()

    @staticmethod
    def set_outgoing_data(buffer):
        """ To set the message the process would send out over the network
        :param buffer:  a python list of characters represent the outgoing message
        :return: no return value
        """
        SenderProcess.__buffer = buffer
        return

    @staticmethod
    def get_outgoing_data():
        """ To get the message the process would send out over the network
        :return:  a python list of characters represent the outgoing message
        """
        return SenderProcess.__buffer


class RDTSender:
    """ Implement the Reliable Data Transfer Protocol V2.2 Sender Side """

    def __init__(self, net_srv):
        """ This is a class constructor
            It initialize the RDT sender sequence number  to '0' and the network layer services
            The network layer service provide the method udt_send(send_pkt)
        """
        self.sequence = '0'
        self.net_srv = net_srv

    @staticmethod
    def get_checksum(data):
        """ Calculate the checksum for outgoing data
        :param data: one and only one character, for example data = 'A'
        :return: the ASCII code of the character, for example ASCII('A') = 65
        """
        "CHANGED"
        # TODO provide your own implementation
        checksum = ord(data)  # you need to change that 
        return checksum

    @staticmethod
    def clone_packet(packet):
        """ Make a copy of the outgoing packet
        :param packet: a python dictionary represent a packet
        :return: return a packet as python dictionary
        """
        pkt_clone = {
            'sequence_number': packet['sequence_number'],
            'data': packet['data'],
            'checksum': packet['checksum']
        }
        return pkt_clone

    @staticmethod
    def is_corrupted(reply):
        """ Check if the received reply from receiver is corrupted or not
        :param reply: a python dictionary represent a reply sent by the receiver
        :return: True -> if the reply is corrupted | False ->  if the reply is NOT corrupted
        """
        # TODO provide your own implementation
        "check reply is corpputed by ack or checksum ack if not 1 0 and checksum if char then corrupted" "CHANGED"
        "When calling get_checksum using RDTSender because methods are static"
        if (reply['ack'] !='1' and reply['ack'] !='0')  or  reply['checksum']!=RDTSender.get_checksum(reply['ack']):
           return True
        return False
        
        pass

    @staticmethod
    def is_expected_seq(reply, exp_seq):
        """ Check if the received reply from receiver has the expected sequence number
        :param reply: a python dictionary represent a reply sent by the receiver
        :param exp_seq: the sender expected sequence number '0' or '1' represented as a character
        :return: True -> if ack in the reply match the   expected sequence number otherwise False
        """

        "Compare sequence number of reply with exp if identical true else false" "CHANGED"
        # TODO provide your own implementation
        if (reply['ack']==exp_seq) :
            return True
        return False

        pass

    @staticmethod
    def make_pkt(seq, data, checksum):
        "NOTE : NO CHANGEEE"
        """ Create an outgoing packet as a python dictionary
        :param seq: a character represent the sequence number of the packet, the one expected by the receiver '0' or '1'
        :param data: a single character the sender want to send to the receiver
        :param checksum: the checksum of the data the sender will send to the receiver
        :return: a python dictionary represent the packet to be sent
        """
        packet = {
            'sequence_number': seq,
            'data': data,
            'checksum': checksum
        }
        return packet

    def rdt_send(self, process_buffer):
        """ Implement the RDT v2.2 for the sender
        :param process_buffer:  a list storing the message the sender process wish to send to the receiver process
        :return: terminate without returning any value
        """

        # for every character in the buffer
        for data in process_buffer:
            checksum = RDTSender.get_checksum(data)
            pkt = RDTSender.make_pkt(self.sequence, data, checksum)
            while(True):
                clonepkt=self.clone_packet(pkt)
                print(f'SENDER Expecting sequence number:',self.sequence)
                print(f'SENDER sending:',clonepkt)
                reply = self.net_srv.udt_send(clonepkt)
                if(self.is_corrupted(reply) or (self.is_expected_seq(reply,self.sequence))==False):
                    print(f'network_layer:corruption occured',reply)#LOOP HERE
                else:
                    if(self.sequence=='0'):
                        self.sequence='1'
                    else:
                        self.sequence='0'    #Flip sequence number after sending packet if not corrupted
                    break
                        


                
            


                             
            
            "NOTE: Code that handles failures and corruption HERE"

        print(f'Sender Done!')
        return
