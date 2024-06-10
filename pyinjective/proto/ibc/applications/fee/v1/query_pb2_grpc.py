# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from pyinjective.proto.ibc.applications.fee.v1 import query_pb2 as ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2

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
        + f' but the generated code in ibc/applications/fee/v1/query_pb2_grpc.py depends on'
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
        + f' but the generated code in ibc/applications/fee/v1/query_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class QueryStub(object):
    """Query defines the ICS29 gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.IncentivizedPackets = channel.unary_unary(
                '/ibc.applications.fee.v1.Query/IncentivizedPackets',
                request_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketsRequest.SerializeToString,
                response_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketsResponse.FromString,
                _registered_method=True)
        self.IncentivizedPacket = channel.unary_unary(
                '/ibc.applications.fee.v1.Query/IncentivizedPacket',
                request_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketRequest.SerializeToString,
                response_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketResponse.FromString,
                _registered_method=True)
        self.IncentivizedPacketsForChannel = channel.unary_unary(
                '/ibc.applications.fee.v1.Query/IncentivizedPacketsForChannel',
                request_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketsForChannelRequest.SerializeToString,
                response_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketsForChannelResponse.FromString,
                _registered_method=True)
        self.TotalRecvFees = channel.unary_unary(
                '/ibc.applications.fee.v1.Query/TotalRecvFees',
                request_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalRecvFeesRequest.SerializeToString,
                response_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalRecvFeesResponse.FromString,
                _registered_method=True)
        self.TotalAckFees = channel.unary_unary(
                '/ibc.applications.fee.v1.Query/TotalAckFees',
                request_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalAckFeesRequest.SerializeToString,
                response_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalAckFeesResponse.FromString,
                _registered_method=True)
        self.TotalTimeoutFees = channel.unary_unary(
                '/ibc.applications.fee.v1.Query/TotalTimeoutFees',
                request_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalTimeoutFeesRequest.SerializeToString,
                response_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalTimeoutFeesResponse.FromString,
                _registered_method=True)
        self.Payee = channel.unary_unary(
                '/ibc.applications.fee.v1.Query/Payee',
                request_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryPayeeRequest.SerializeToString,
                response_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryPayeeResponse.FromString,
                _registered_method=True)
        self.CounterpartyPayee = channel.unary_unary(
                '/ibc.applications.fee.v1.Query/CounterpartyPayee',
                request_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryCounterpartyPayeeRequest.SerializeToString,
                response_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryCounterpartyPayeeResponse.FromString,
                _registered_method=True)
        self.FeeEnabledChannels = channel.unary_unary(
                '/ibc.applications.fee.v1.Query/FeeEnabledChannels',
                request_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryFeeEnabledChannelsRequest.SerializeToString,
                response_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryFeeEnabledChannelsResponse.FromString,
                _registered_method=True)
        self.FeeEnabledChannel = channel.unary_unary(
                '/ibc.applications.fee.v1.Query/FeeEnabledChannel',
                request_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryFeeEnabledChannelRequest.SerializeToString,
                response_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryFeeEnabledChannelResponse.FromString,
                _registered_method=True)


class QueryServicer(object):
    """Query defines the ICS29 gRPC querier service.
    """

    def IncentivizedPackets(self, request, context):
        """IncentivizedPackets returns all incentivized packets and their associated fees
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IncentivizedPacket(self, request, context):
        """IncentivizedPacket returns all packet fees for a packet given its identifier
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IncentivizedPacketsForChannel(self, request, context):
        """Gets all incentivized packets for a specific channel
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TotalRecvFees(self, request, context):
        """TotalRecvFees returns the total receive fees for a packet given its identifier
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TotalAckFees(self, request, context):
        """TotalAckFees returns the total acknowledgement fees for a packet given its identifier
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TotalTimeoutFees(self, request, context):
        """TotalTimeoutFees returns the total timeout fees for a packet given its identifier
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Payee(self, request, context):
        """Payee returns the registered payee address for a specific channel given the relayer address
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CounterpartyPayee(self, request, context):
        """CounterpartyPayee returns the registered counterparty payee for forward relaying
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FeeEnabledChannels(self, request, context):
        """FeeEnabledChannels returns a list of all fee enabled channels
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FeeEnabledChannel(self, request, context):
        """FeeEnabledChannel returns true if the provided port and channel identifiers belong to a fee enabled channel
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'IncentivizedPackets': grpc.unary_unary_rpc_method_handler(
                    servicer.IncentivizedPackets,
                    request_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketsRequest.FromString,
                    response_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketsResponse.SerializeToString,
            ),
            'IncentivizedPacket': grpc.unary_unary_rpc_method_handler(
                    servicer.IncentivizedPacket,
                    request_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketRequest.FromString,
                    response_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketResponse.SerializeToString,
            ),
            'IncentivizedPacketsForChannel': grpc.unary_unary_rpc_method_handler(
                    servicer.IncentivizedPacketsForChannel,
                    request_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketsForChannelRequest.FromString,
                    response_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketsForChannelResponse.SerializeToString,
            ),
            'TotalRecvFees': grpc.unary_unary_rpc_method_handler(
                    servicer.TotalRecvFees,
                    request_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalRecvFeesRequest.FromString,
                    response_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalRecvFeesResponse.SerializeToString,
            ),
            'TotalAckFees': grpc.unary_unary_rpc_method_handler(
                    servicer.TotalAckFees,
                    request_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalAckFeesRequest.FromString,
                    response_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalAckFeesResponse.SerializeToString,
            ),
            'TotalTimeoutFees': grpc.unary_unary_rpc_method_handler(
                    servicer.TotalTimeoutFees,
                    request_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalTimeoutFeesRequest.FromString,
                    response_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalTimeoutFeesResponse.SerializeToString,
            ),
            'Payee': grpc.unary_unary_rpc_method_handler(
                    servicer.Payee,
                    request_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryPayeeRequest.FromString,
                    response_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryPayeeResponse.SerializeToString,
            ),
            'CounterpartyPayee': grpc.unary_unary_rpc_method_handler(
                    servicer.CounterpartyPayee,
                    request_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryCounterpartyPayeeRequest.FromString,
                    response_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryCounterpartyPayeeResponse.SerializeToString,
            ),
            'FeeEnabledChannels': grpc.unary_unary_rpc_method_handler(
                    servicer.FeeEnabledChannels,
                    request_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryFeeEnabledChannelsRequest.FromString,
                    response_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryFeeEnabledChannelsResponse.SerializeToString,
            ),
            'FeeEnabledChannel': grpc.unary_unary_rpc_method_handler(
                    servicer.FeeEnabledChannel,
                    request_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryFeeEnabledChannelRequest.FromString,
                    response_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryFeeEnabledChannelResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ibc.applications.fee.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ibc.applications.fee.v1.Query', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Query defines the ICS29 gRPC querier service.
    """

    @staticmethod
    def IncentivizedPackets(request,
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
            '/ibc.applications.fee.v1.Query/IncentivizedPackets',
            ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketsRequest.SerializeToString,
            ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketsResponse.FromString,
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
    def IncentivizedPacket(request,
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
            '/ibc.applications.fee.v1.Query/IncentivizedPacket',
            ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketRequest.SerializeToString,
            ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketResponse.FromString,
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
    def IncentivizedPacketsForChannel(request,
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
            '/ibc.applications.fee.v1.Query/IncentivizedPacketsForChannel',
            ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketsForChannelRequest.SerializeToString,
            ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketsForChannelResponse.FromString,
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
    def TotalRecvFees(request,
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
            '/ibc.applications.fee.v1.Query/TotalRecvFees',
            ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalRecvFeesRequest.SerializeToString,
            ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalRecvFeesResponse.FromString,
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
    def TotalAckFees(request,
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
            '/ibc.applications.fee.v1.Query/TotalAckFees',
            ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalAckFeesRequest.SerializeToString,
            ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalAckFeesResponse.FromString,
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
    def TotalTimeoutFees(request,
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
            '/ibc.applications.fee.v1.Query/TotalTimeoutFees',
            ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalTimeoutFeesRequest.SerializeToString,
            ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalTimeoutFeesResponse.FromString,
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
    def Payee(request,
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
            '/ibc.applications.fee.v1.Query/Payee',
            ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryPayeeRequest.SerializeToString,
            ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryPayeeResponse.FromString,
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
    def CounterpartyPayee(request,
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
            '/ibc.applications.fee.v1.Query/CounterpartyPayee',
            ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryCounterpartyPayeeRequest.SerializeToString,
            ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryCounterpartyPayeeResponse.FromString,
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
    def FeeEnabledChannels(request,
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
            '/ibc.applications.fee.v1.Query/FeeEnabledChannels',
            ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryFeeEnabledChannelsRequest.SerializeToString,
            ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryFeeEnabledChannelsResponse.FromString,
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
    def FeeEnabledChannel(request,
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
            '/ibc.applications.fee.v1.Query/FeeEnabledChannel',
            ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryFeeEnabledChannelRequest.SerializeToString,
            ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryFeeEnabledChannelResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
