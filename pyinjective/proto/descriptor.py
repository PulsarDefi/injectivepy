from google.protobuf import descriptor_pb2
from google.protobuf.descriptor_pool import DescriptorPool

INJECTIVE_DESCRIPTOR_POOL = DescriptorPool()
file_descriptor_proto = descriptor_pb2.FileDescriptorProto()
descriptor_pb2.DESCRIPTOR.CopyToProto(file_descriptor_proto)
INJECTIVE_DESCRIPTOR_POOL.pool.Add(file_descriptor_proto)
