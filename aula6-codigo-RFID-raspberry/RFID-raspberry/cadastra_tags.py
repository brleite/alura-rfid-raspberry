import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('tags')


cartoes = {
    '1971212171110' : 'ricardo',
    '1971212171111' : 'teste',
    '1971212171112' : 'teste2'
}


for id, usuario in cartoes.items():
    table.put_item(
        Item={
            'id': id,
            'usuario': usuario
        }
    )
    print(id, ': ', usuario)

