# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from protos import distributedML_pb2 as protos_dot_distributedML__pb2


class ParamFeederStub(object):
  """Main server for passing infromation around
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SendParams = channel.unary_stream(
        '/distributedML.ParamFeeder/SendParams',
        request_serializer=protos_dot_distributedML__pb2.WorkerInfo.SerializeToString,
        response_deserializer=protos_dot_distributedML__pb2.SubTensor.FromString,
        )
    self.SendNextBatch = channel.unary_unary(
        '/distributedML.ParamFeeder/SendNextBatch',
        request_serializer=protos_dot_distributedML__pb2.PrevBatch.SerializeToString,
        response_deserializer=protos_dot_distributedML__pb2.NextBatch.FromString,
        )
    self.GetUpdates = channel.stream_unary(
        '/distributedML.ParamFeeder/GetUpdates',
        request_serializer=protos_dot_distributedML__pb2.SubTensor.SerializeToString,
        response_deserializer=protos_dot_distributedML__pb2.StatusCode.FromString,
        )
    self.ping = channel.unary_unary(
        '/distributedML.ParamFeeder/ping',
        request_serializer=protos_dot_distributedML__pb2.empty.SerializeToString,
        response_deserializer=protos_dot_distributedML__pb2.empty.FromString,
        )


class ParamFeederServicer(object):
  """Main server for passing infromation around
  """

  def SendParams(self, request, context):
    """Sends the parameters back and forth between server and worker
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendNextBatch(self, request, context):
    """Sends information about the next batch
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUpdates(self, request_iterator, context):
    """Gets gardient updates from client servers
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ping(self, request, context):
    """This call simply makes sure that all machines have begun to run Paxos. 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ParamFeederServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SendParams': grpc.unary_stream_rpc_method_handler(
          servicer.SendParams,
          request_deserializer=protos_dot_distributedML__pb2.WorkerInfo.FromString,
          response_serializer=protos_dot_distributedML__pb2.SubTensor.SerializeToString,
      ),
      'SendNextBatch': grpc.unary_unary_rpc_method_handler(
          servicer.SendNextBatch,
          request_deserializer=protos_dot_distributedML__pb2.PrevBatch.FromString,
          response_serializer=protos_dot_distributedML__pb2.NextBatch.SerializeToString,
      ),
      'GetUpdates': grpc.stream_unary_rpc_method_handler(
          servicer.GetUpdates,
          request_deserializer=protos_dot_distributedML__pb2.SubTensor.FromString,
          response_serializer=protos_dot_distributedML__pb2.StatusCode.SerializeToString,
      ),
      'ping': grpc.unary_unary_rpc_method_handler(
          servicer.ping,
          request_deserializer=protos_dot_distributedML__pb2.empty.FromString,
          response_serializer=protos_dot_distributedML__pb2.empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'distributedML.ParamFeeder', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))