# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from pyinjective.proto.exchange import injective_exchange_rpc_pb2 as exchange_dot_injective__exchange__rpc__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in exchange/injective_exchange_rpc_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in exchange/injective_exchange_rpc_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class InjectiveExchangeRPCStub(object):
    """InjectiveExchangeRPC defines gRPC API of an Injective Exchange service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTx = channel.unary_unary(
                '/injective_exchange_rpc.InjectiveExchangeRPC/GetTx',
                request_serializer=exchange_dot_injective__exchange__rpc__pb2.GetTxRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__exchange__rpc__pb2.GetTxResponse.FromString,
                _registered_method=True)
        self.PrepareTx = channel.unary_unary(
                '/injective_exchange_rpc.InjectiveExchangeRPC/PrepareTx',
                request_serializer=exchange_dot_injective__exchange__rpc__pb2.PrepareTxRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__exchange__rpc__pb2.PrepareTxResponse.FromString,
                _registered_method=True)
        self.BroadcastTx = channel.unary_unary(
                '/injective_exchange_rpc.InjectiveExchangeRPC/BroadcastTx',
                request_serializer=exchange_dot_injective__exchange__rpc__pb2.BroadcastTxRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__exchange__rpc__pb2.BroadcastTxResponse.FromString,
                _registered_method=True)
        self.PrepareCosmosTx = channel.unary_unary(
                '/injective_exchange_rpc.InjectiveExchangeRPC/PrepareCosmosTx',
                request_serializer=exchange_dot_injective__exchange__rpc__pb2.PrepareCosmosTxRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__exchange__rpc__pb2.PrepareCosmosTxResponse.FromString,
                _registered_method=True)
        self.BroadcastCosmosTx = channel.unary_unary(
                '/injective_exchange_rpc.InjectiveExchangeRPC/BroadcastCosmosTx',
                request_serializer=exchange_dot_injective__exchange__rpc__pb2.BroadcastCosmosTxRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__exchange__rpc__pb2.BroadcastCosmosTxResponse.FromString,
                _registered_method=True)
        self.GetFeePayer = channel.unary_unary(
                '/injective_exchange_rpc.InjectiveExchangeRPC/GetFeePayer',
                request_serializer=exchange_dot_injective__exchange__rpc__pb2.GetFeePayerRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__exchange__rpc__pb2.GetFeePayerResponse.FromString,
                _registered_method=True)


class InjectiveExchangeRPCServicer(object):
    """InjectiveExchangeRPC defines gRPC API of an Injective Exchange service.
    """

    def GetTx(self, request, context):
        """GetTx gets transaction details by hash.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PrepareTx(self, request, context):
        """PrepareTx generates a Web3-signable body for a Cosmos transaction
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BroadcastTx(self, request, context):
        """BroadcastTx broadcasts a signed Web3 transaction
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PrepareCosmosTx(self, request, context):
        """PrepareCosmosTx generates a Web3-signable body for a Cosmos transaction
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BroadcastCosmosTx(self, request, context):
        """BroadcastCosmosTx broadcasts a signed Web3 transaction
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFeePayer(self, request, context):
        """Return fee payer information's
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InjectiveExchangeRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTx': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTx,
                    request_deserializer=exchange_dot_injective__exchange__rpc__pb2.GetTxRequest.FromString,
                    response_serializer=exchange_dot_injective__exchange__rpc__pb2.GetTxResponse.SerializeToString,
            ),
            'PrepareTx': grpc.unary_unary_rpc_method_handler(
                    servicer.PrepareTx,
                    request_deserializer=exchange_dot_injective__exchange__rpc__pb2.PrepareTxRequest.FromString,
                    response_serializer=exchange_dot_injective__exchange__rpc__pb2.PrepareTxResponse.SerializeToString,
            ),
            'BroadcastTx': grpc.unary_unary_rpc_method_handler(
                    servicer.BroadcastTx,
                    request_deserializer=exchange_dot_injective__exchange__rpc__pb2.BroadcastTxRequest.FromString,
                    response_serializer=exchange_dot_injective__exchange__rpc__pb2.BroadcastTxResponse.SerializeToString,
            ),
            'PrepareCosmosTx': grpc.unary_unary_rpc_method_handler(
                    servicer.PrepareCosmosTx,
                    request_deserializer=exchange_dot_injective__exchange__rpc__pb2.PrepareCosmosTxRequest.FromString,
                    response_serializer=exchange_dot_injective__exchange__rpc__pb2.PrepareCosmosTxResponse.SerializeToString,
            ),
            'BroadcastCosmosTx': grpc.unary_unary_rpc_method_handler(
                    servicer.BroadcastCosmosTx,
                    request_deserializer=exchange_dot_injective__exchange__rpc__pb2.BroadcastCosmosTxRequest.FromString,
                    response_serializer=exchange_dot_injective__exchange__rpc__pb2.BroadcastCosmosTxResponse.SerializeToString,
            ),
            'GetFeePayer': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFeePayer,
                    request_deserializer=exchange_dot_injective__exchange__rpc__pb2.GetFeePayerRequest.FromString,
                    response_serializer=exchange_dot_injective__exchange__rpc__pb2.GetFeePayerResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective_exchange_rpc.InjectiveExchangeRPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('injective_exchange_rpc.InjectiveExchangeRPC', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class InjectiveExchangeRPC(object):
    """InjectiveExchangeRPC defines gRPC API of an Injective Exchange service.
    """

    @staticmethod
    def GetTx(request,
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
            '/injective_exchange_rpc.InjectiveExchangeRPC/GetTx',
            exchange_dot_injective__exchange__rpc__pb2.GetTxRequest.SerializeToString,
            exchange_dot_injective__exchange__rpc__pb2.GetTxResponse.FromString,
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
    def PrepareTx(request,
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
            '/injective_exchange_rpc.InjectiveExchangeRPC/PrepareTx',
            exchange_dot_injective__exchange__rpc__pb2.PrepareTxRequest.SerializeToString,
            exchange_dot_injective__exchange__rpc__pb2.PrepareTxResponse.FromString,
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
    def BroadcastTx(request,
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
            '/injective_exchange_rpc.InjectiveExchangeRPC/BroadcastTx',
            exchange_dot_injective__exchange__rpc__pb2.BroadcastTxRequest.SerializeToString,
            exchange_dot_injective__exchange__rpc__pb2.BroadcastTxResponse.FromString,
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
    def PrepareCosmosTx(request,
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
            '/injective_exchange_rpc.InjectiveExchangeRPC/PrepareCosmosTx',
            exchange_dot_injective__exchange__rpc__pb2.PrepareCosmosTxRequest.SerializeToString,
            exchange_dot_injective__exchange__rpc__pb2.PrepareCosmosTxResponse.FromString,
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
    def BroadcastCosmosTx(request,
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
            '/injective_exchange_rpc.InjectiveExchangeRPC/BroadcastCosmosTx',
            exchange_dot_injective__exchange__rpc__pb2.BroadcastCosmosTxRequest.SerializeToString,
            exchange_dot_injective__exchange__rpc__pb2.BroadcastCosmosTxResponse.FromString,
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
    def GetFeePayer(request,
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
            '/injective_exchange_rpc.InjectiveExchangeRPC/GetFeePayer',
            exchange_dot_injective__exchange__rpc__pb2.GetFeePayerRequest.SerializeToString,
            exchange_dot_injective__exchange__rpc__pb2.GetFeePayerResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
