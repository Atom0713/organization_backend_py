from ariadne import QueryType, make_executable_schema, load_schema_from_path
from ..controller.query_resolver import getAllPlayers, getAllStaff

type_defs = load_schema_from_path("src\service\graphql\schema.graphql")


query = QueryType()


@query.field("getAllPlayers")
def resolve_get_post(_, info):
    # request = info.context
    # user_agent = request.headers.get("User-Agent", "Guest")
    return getAllPlayers()

@query.field("getAllStaff")
def resolve_get_post(_, info):
    # request = info.context
    # user_agent = request.headers.get("User-Agent", "Guest")
    return getAllStaff()

schema = make_executable_schema(type_defs, query)
