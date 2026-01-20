from translator.ir import IRFunction, IRModule


def build_ir(knowledge_objects, call_graph):
    functions = []

    for ko in knowledge_objects:
        if ko.type == "function":
            functions.append(
                IRFunction(
                    name=ko.name,
                    args=[],                 # can infer later
                    return_type=None,
                    body_logic=ko.code,
                    calls=ko.calls,
                    description=ko.summary
                )
            )

    return IRModule(
        functions=functions,
        imports=[]
    )
