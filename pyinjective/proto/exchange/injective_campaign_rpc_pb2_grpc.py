# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from pyinjective.proto.exchange import injective_campaign_rpc_pb2 as exchange_dot_injective__campaign__rpc__pb2

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
        + f' but the generated code in exchange/injective_campaign_rpc_pb2_grpc.py depends on'
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
        + f' but the generated code in exchange/injective_campaign_rpc_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class InjectiveCampaignRPCStub(object):
    """InjectiveCampaignRPC defined a gRPC service for Injective Campaigns.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ranking = channel.unary_unary(
                '/injective_campaign_rpc.InjectiveCampaignRPC/Ranking',
                request_serializer=exchange_dot_injective__campaign__rpc__pb2.RankingRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__campaign__rpc__pb2.RankingResponse.FromString,
                _registered_method=True)
        self.Campaigns = channel.unary_unary(
                '/injective_campaign_rpc.InjectiveCampaignRPC/Campaigns',
                request_serializer=exchange_dot_injective__campaign__rpc__pb2.CampaignsRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__campaign__rpc__pb2.CampaignsResponse.FromString,
                _registered_method=True)
        self.ListGuilds = channel.unary_unary(
                '/injective_campaign_rpc.InjectiveCampaignRPC/ListGuilds',
                request_serializer=exchange_dot_injective__campaign__rpc__pb2.ListGuildsRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__campaign__rpc__pb2.ListGuildsResponse.FromString,
                _registered_method=True)
        self.ListGuildMembers = channel.unary_unary(
                '/injective_campaign_rpc.InjectiveCampaignRPC/ListGuildMembers',
                request_serializer=exchange_dot_injective__campaign__rpc__pb2.ListGuildMembersRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__campaign__rpc__pb2.ListGuildMembersResponse.FromString,
                _registered_method=True)
        self.GetGuildMember = channel.unary_unary(
                '/injective_campaign_rpc.InjectiveCampaignRPC/GetGuildMember',
                request_serializer=exchange_dot_injective__campaign__rpc__pb2.GetGuildMemberRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__campaign__rpc__pb2.GetGuildMemberResponse.FromString,
                _registered_method=True)


class InjectiveCampaignRPCServicer(object):
    """InjectiveCampaignRPC defined a gRPC service for Injective Campaigns.
    """

    def Ranking(self, request, context):
        """Lists all participants in campaign
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Campaigns(self, request, context):
        """List current round active campaigns
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListGuilds(self, request, context):
        """List guilds by campaign
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListGuildMembers(self, request, context):
        """List guild members of given campaign and guildId
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetGuildMember(self, request, context):
        """Get single member guild info
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InjectiveCampaignRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Ranking': grpc.unary_unary_rpc_method_handler(
                    servicer.Ranking,
                    request_deserializer=exchange_dot_injective__campaign__rpc__pb2.RankingRequest.FromString,
                    response_serializer=exchange_dot_injective__campaign__rpc__pb2.RankingResponse.SerializeToString,
            ),
            'Campaigns': grpc.unary_unary_rpc_method_handler(
                    servicer.Campaigns,
                    request_deserializer=exchange_dot_injective__campaign__rpc__pb2.CampaignsRequest.FromString,
                    response_serializer=exchange_dot_injective__campaign__rpc__pb2.CampaignsResponse.SerializeToString,
            ),
            'ListGuilds': grpc.unary_unary_rpc_method_handler(
                    servicer.ListGuilds,
                    request_deserializer=exchange_dot_injective__campaign__rpc__pb2.ListGuildsRequest.FromString,
                    response_serializer=exchange_dot_injective__campaign__rpc__pb2.ListGuildsResponse.SerializeToString,
            ),
            'ListGuildMembers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListGuildMembers,
                    request_deserializer=exchange_dot_injective__campaign__rpc__pb2.ListGuildMembersRequest.FromString,
                    response_serializer=exchange_dot_injective__campaign__rpc__pb2.ListGuildMembersResponse.SerializeToString,
            ),
            'GetGuildMember': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGuildMember,
                    request_deserializer=exchange_dot_injective__campaign__rpc__pb2.GetGuildMemberRequest.FromString,
                    response_serializer=exchange_dot_injective__campaign__rpc__pb2.GetGuildMemberResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective_campaign_rpc.InjectiveCampaignRPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('injective_campaign_rpc.InjectiveCampaignRPC', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class InjectiveCampaignRPC(object):
    """InjectiveCampaignRPC defined a gRPC service for Injective Campaigns.
    """

    @staticmethod
    def Ranking(request,
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
            '/injective_campaign_rpc.InjectiveCampaignRPC/Ranking',
            exchange_dot_injective__campaign__rpc__pb2.RankingRequest.SerializeToString,
            exchange_dot_injective__campaign__rpc__pb2.RankingResponse.FromString,
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
    def Campaigns(request,
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
            '/injective_campaign_rpc.InjectiveCampaignRPC/Campaigns',
            exchange_dot_injective__campaign__rpc__pb2.CampaignsRequest.SerializeToString,
            exchange_dot_injective__campaign__rpc__pb2.CampaignsResponse.FromString,
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
    def ListGuilds(request,
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
            '/injective_campaign_rpc.InjectiveCampaignRPC/ListGuilds',
            exchange_dot_injective__campaign__rpc__pb2.ListGuildsRequest.SerializeToString,
            exchange_dot_injective__campaign__rpc__pb2.ListGuildsResponse.FromString,
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
    def ListGuildMembers(request,
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
            '/injective_campaign_rpc.InjectiveCampaignRPC/ListGuildMembers',
            exchange_dot_injective__campaign__rpc__pb2.ListGuildMembersRequest.SerializeToString,
            exchange_dot_injective__campaign__rpc__pb2.ListGuildMembersResponse.FromString,
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
    def GetGuildMember(request,
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
            '/injective_campaign_rpc.InjectiveCampaignRPC/GetGuildMember',
            exchange_dot_injective__campaign__rpc__pb2.GetGuildMemberRequest.SerializeToString,
            exchange_dot_injective__campaign__rpc__pb2.GetGuildMemberResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
