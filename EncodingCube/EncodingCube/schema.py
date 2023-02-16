import graphene
import Encryption.schema

class Query(Encryption.schema.Query, graphene.ObjectType):
    pass

class Mutation(Encryption.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation) 