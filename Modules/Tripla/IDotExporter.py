import graphviz

class IDotExporter:
    def to_dot_parse(self,dot):
        pass
    def to_dot_ast(self,dot):
        pass

    def getNodeString(self):
        return "node_"+str(self.pp)

    def getParseTree(self):
        dot = graphviz.Digraph('Parse-Tree', comment='Parse-Tree')
        dot.attr(bgcolor='#282a36')

        dot.attr('node', color='white', fontcolor='white')
        dot.attr('edge', color='white', fontcolor='white')
        self.to_dot_parse(dot)
        return dot

    def getAstTree(self):
        dot = graphviz.Digraph('Ast-Tree', comment='Ast-Tree')
        dot.attr(bgcolor='#282a36')

        dot.attr('node', color='white', fontcolor='white')
        dot.attr('edge', color='white', fontcolor='white')
        self.to_dot_ast(dot)
        return dot
