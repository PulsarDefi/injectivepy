# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from exchange import injective_dmm_rpc_pb2 as exchange_dot_injective__dmm__rpc__pb2


class InjectiveDmmRPCStub(object):
    """InjectiveDmmRPC defines gRPC API of DMM Dashboard.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetEpochs = channel.unary_unary(
                '/injective_dmm_rpc.InjectiveDmmRPC/GetEpochs',
                request_serializer=exchange_dot_injective__dmm__rpc__pb2.GetEpochsRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__dmm__rpc__pb2.GetEpochsResponse.FromString,
                )
        self.GetEpochSummary = channel.unary_unary(
                '/injective_dmm_rpc.InjectiveDmmRPC/GetEpochSummary',
                request_serializer=exchange_dot_injective__dmm__rpc__pb2.GetEpochSummaryRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__dmm__rpc__pb2.GetEpochSummaryResponse.FromString,
                )
        self.GetDMMRecords = channel.unary_unary(
                '/injective_dmm_rpc.InjectiveDmmRPC/GetDMMRecords',
                request_serializer=exchange_dot_injective__dmm__rpc__pb2.GetDMMRecordsRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__dmm__rpc__pb2.GetDMMRecordsResponse.FromString,
                )


class InjectiveDmmRPCServicer(object):
    """InjectiveDmmRPC defines gRPC API of DMM Dashboard.
    """

    def GetEpochs(self, request, context):
        """Get all passed epochs and the current or next incoming epoch
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEpochSummary(self, request, context):
        """Get epoch summary by epoch id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDMMRecords(self, request, context):
        """Get all epoch result records for one dmm
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InjectiveDmmRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetEpochs': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEpochs,
                    request_deserializer=exchange_dot_injective__dmm__rpc__pb2.GetEpochsRequest.FromString,
                    response_serializer=exchange_dot_injective__dmm__rpc__pb2.GetEpochsResponse.SerializeToString,
            ),
            'GetEpochSummary': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEpochSummary,
                    request_deserializer=exchange_dot_injective__dmm__rpc__pb2.GetEpochSummaryRequest.FromString,
                    response_serializer=exchange_dot_injective__dmm__rpc__pb2.GetEpochSummaryResponse.SerializeToString,
            ),
            'GetDMMRecords': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDMMRecords,
                    request_deserializer=exchange_dot_injective__dmm__rpc__pb2.GetDMMRecordsRequest.FromString,
                    response_serializer=exchange_dot_injective__dmm__rpc__pb2.GetDMMRecordsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective_dmm_rpc.InjectiveDmmRPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InjectiveDmmRPC(object):
    """InjectiveDmmRPC defines gRPC API of DMM Dashboard.
    """

    @staticmethod
    def GetEpochs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_dmm_rpc.InjectiveDmmRPC/GetEpochs',
            exchange_dot_injective__dmm__rpc__pb2.GetEpochsRequest.SerializeToString,
            exchange_dot_injective__dmm__rpc__pb2.GetEpochsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEpochSummary(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_dmm_rpc.InjectiveDmmRPC/GetEpochSummary',
            exchange_dot_injective__dmm__rpc__pb2.GetEpochSummaryRequest.SerializeToString,
            exchange_dot_injective__dmm__rpc__pb2.GetEpochSummaryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDMMRecords(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_dmm_rpc.InjectiveDmmRPC/GetDMMRecords',
            exchange_dot_injective__dmm__rpc__pb2.GetDMMRecordsRequest.SerializeToString,
            exchange_dot_injective__dmm__rpc__pb2.GetDMMRecordsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
