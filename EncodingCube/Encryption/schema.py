import graphene

class EncryptedTextType(graphene.ObjectType):
    inputText = graphene.String()
    inputWord = graphene.String()

  
class DecryptedTextType(graphene.ObjectType):
    class Meta: 
        description = 'Decrypted Text'
    
    decrypted = graphene.Field(graphene.String)


class Query(graphene.ObjectType):
    encrypted = graphene.Field(EncryptedTextType)

    def resolve_encrypted(root, info, **kwargs):
        return  info.context.get('encrypted')

class CreateEncryptedText(graphene.Mutation):
    class Arguments:
        inputText = graphene.String(required=True)
        inputWord = graphene.String(required=True)

    encryptedText = graphene.Field(EncryptedTextType)

    @classmethod
    def mutate(self, inputText, inputWord):
        encrypted = EncryptedTextType()
        encrypted.inputText = inputText
        encrypted.inputWord = inputWord
        
        return CreateEncryptedText(encryptedText=encrypted)

class Mutation(graphene.ObjectType):
    create_encryptedText = CreateEncryptedText.Field()