# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import aruco_pb2 as aruco__pb2


class GreeterStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SayHello = channel.unary_unary(
        '/aruco.Greeter/SayHello',
        request_serializer=aruco__pb2.Empty.SerializeToString,
        response_deserializer=aruco__pb2.HelloReply.FromString,
        )
    self.Ask = channel.unary_unary(
        '/aruco.Greeter/Ask',
        request_serializer=aruco__pb2.Empty.SerializeToString,
        response_deserializer=aruco__pb2.Coordinate.FromString,
        )
    self.Goal = channel.unary_unary(
        '/aruco.Greeter/Goal',
        request_serializer=aruco__pb2.Empty.SerializeToString,
        response_deserializer=aruco__pb2.Coordinate.FromString,
        )


class GreeterServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SayHello(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Ask(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Goal(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SayHello': grpc.unary_unary_rpc_method_handler(
          servicer.SayHello,
          request_deserializer=aruco__pb2.Empty.FromString,
          response_serializer=aruco__pb2.HelloReply.SerializeToString,
      ),
      'Ask': grpc.unary_unary_rpc_method_handler(
          servicer.Ask,
          request_deserializer=aruco__pb2.Empty.FromString,
          response_serializer=aruco__pb2.Coordinate.SerializeToString,
      ),
      'Goal': grpc.unary_unary_rpc_method_handler(
          servicer.Goal,
          request_deserializer=aruco__pb2.Empty.FromString,
          response_serializer=aruco__pb2.Coordinate.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'aruco.Greeter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))