# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from injective_proto.proto.injective.stream.v1beta1 import query_pb2 as injective_dot_stream_dot_v1beta1_dot_query__pb2


class StreamStub(object):
    """ChainStream defines the gRPC streaming service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Stream = channel.unary_stream(
                '/injective.stream.v1beta1.Stream/Stream',
                request_serializer=injective_dot_stream_dot_v1beta1_dot_query__pb2.StreamRequest.SerializeToString,
                response_deserializer=injective_dot_stream_dot_v1beta1_dot_query__pb2.StreamResponse.FromString,
                _registered_method=True)


class StreamServicer(object):
    """ChainStream defines the gRPC streaming service.
    """

    def Stream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StreamServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Stream': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream,
                    request_deserializer=injective_dot_stream_dot_v1beta1_dot_query__pb2.StreamRequest.FromString,
                    response_serializer=injective_dot_stream_dot_v1beta1_dot_query__pb2.StreamResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective.stream.v1beta1.Stream', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('injective.stream.v1beta1.Stream', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Stream(object):
    """ChainStream defines the gRPC streaming service.
    """

    @staticmethod
    def Stream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/injective.stream.v1beta1.Stream/Stream',
            injective_dot_stream_dot_v1beta1_dot_query__pb2.StreamRequest.SerializeToString,
            injective_dot_stream_dot_v1beta1_dot_query__pb2.StreamResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
