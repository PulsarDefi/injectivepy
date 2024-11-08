# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from injective_proto.proto.exchange import injective_archiver_rpc_pb2 as exchange_dot_injective__archiver__rpc__pb2


class InjectiveArchiverRPCStub(object):
    """InjectiveArchiverRPC defines gRPC API of Archiver provider.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Balance = channel.unary_unary(
                '/injective_archiver_rpc.InjectiveArchiverRPC/Balance',
                request_serializer=exchange_dot_injective__archiver__rpc__pb2.BalanceRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__archiver__rpc__pb2.BalanceResponse.FromString,
                _registered_method=True)
        self.Rpnl = channel.unary_unary(
                '/injective_archiver_rpc.InjectiveArchiverRPC/Rpnl',
                request_serializer=exchange_dot_injective__archiver__rpc__pb2.RpnlRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__archiver__rpc__pb2.RpnlResponse.FromString,
                _registered_method=True)
        self.Volumes = channel.unary_unary(
                '/injective_archiver_rpc.InjectiveArchiverRPC/Volumes',
                request_serializer=exchange_dot_injective__archiver__rpc__pb2.VolumesRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__archiver__rpc__pb2.VolumesResponse.FromString,
                _registered_method=True)


class InjectiveArchiverRPCServicer(object):
    """InjectiveArchiverRPC defines gRPC API of Archiver provider.
    """

    def Balance(self, request, context):
        """Provide historical balance data for a given account address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Rpnl(self, request, context):
        """Provide historical realized profit and loss data for a given account address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Volumes(self, request, context):
        """Provide historical volumes for a given account address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InjectiveArchiverRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Balance': grpc.unary_unary_rpc_method_handler(
                    servicer.Balance,
                    request_deserializer=exchange_dot_injective__archiver__rpc__pb2.BalanceRequest.FromString,
                    response_serializer=exchange_dot_injective__archiver__rpc__pb2.BalanceResponse.SerializeToString,
            ),
            'Rpnl': grpc.unary_unary_rpc_method_handler(
                    servicer.Rpnl,
                    request_deserializer=exchange_dot_injective__archiver__rpc__pb2.RpnlRequest.FromString,
                    response_serializer=exchange_dot_injective__archiver__rpc__pb2.RpnlResponse.SerializeToString,
            ),
            'Volumes': grpc.unary_unary_rpc_method_handler(
                    servicer.Volumes,
                    request_deserializer=exchange_dot_injective__archiver__rpc__pb2.VolumesRequest.FromString,
                    response_serializer=exchange_dot_injective__archiver__rpc__pb2.VolumesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective_archiver_rpc.InjectiveArchiverRPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('injective_archiver_rpc.InjectiveArchiverRPC', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class InjectiveArchiverRPC(object):
    """InjectiveArchiverRPC defines gRPC API of Archiver provider.
    """

    @staticmethod
    def Balance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective_archiver_rpc.InjectiveArchiverRPC/Balance',
            exchange_dot_injective__archiver__rpc__pb2.BalanceRequest.SerializeToString,
            exchange_dot_injective__archiver__rpc__pb2.BalanceResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Rpnl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective_archiver_rpc.InjectiveArchiverRPC/Rpnl',
            exchange_dot_injective__archiver__rpc__pb2.RpnlRequest.SerializeToString,
            exchange_dot_injective__archiver__rpc__pb2.RpnlResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Volumes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective_archiver_rpc.InjectiveArchiverRPC/Volumes',
            exchange_dot_injective__archiver__rpc__pb2.VolumesRequest.SerializeToString,
            exchange_dot_injective__archiver__rpc__pb2.VolumesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
