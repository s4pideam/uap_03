class RhoItem:
    label = None
    nl = 0


class ICodeExporter:
    def to_code(self, rho, nl):
        pass


    def getInstructionList(self):
        Label.count = 0
        return self.to_code(dict(),0) + [halt()]

    def getInstructionString(self):
        Label.count = 0
        return '\n'.join([instr.toString() for instr in self.getInstructionList()])


class Label:
    count=0
    address=-1

    def __init__(self,address=-1):
        Label.count+=1
        self.id=Label.count
        self.address=address

    def toString(self): return "L"+str(self.id)

    def create_array(i):
        return [Label() for _ in range(i)]
       

class Instruction:

    def __init__(self,assigned_label=None):
        self.assigned_labels = []
        if not assigned_label is None:
            self.assigned_labels+=[assigned_label]

    def toString(self):
        s=self.labelsToString()
        return(s)

    def labelsToString(self):
        if (len(self.assigned_labels)==0):
            return "\t"
        else:
            return ','.join( [ label.toString()
                               for label in self.assigned_labels] )+":\t"

class halt(Instruction):
    def __init__(self,assigned_label=None):
        super().__init__(assigned_label=assigned_label)

    def toString(self): return super().toString()+"HALT"

class nop(Instruction):
    def __init__(self,assigned_label=None):
        super().__init__(assigned_label=assigned_label)

    def toString(self): return super().toString()+"NOP"

class pop(Instruction):
    def __init__(self,assigned_label=None):
        super().__init__(assigned_label=assigned_label)

    def toString(self): return super().toString()+"POP"

class const(Instruction):
    def __init__(self, k, assigned_label=None):
        super().__init__(assigned_label=assigned_label)
        self.k=k

    def toString(self): return super().toString()+"CONST "+str(int(self.k))

class store(Instruction):
    def __init__(self, k, d, assigned_label=None):
        super().__init__(assigned_label=assigned_label)
        self.k=k
        self.d=d

    def toString(self):
        return super().toString()+"STORE "+str(self.k)+" "+str(self.d)

class load(Instruction):
    def __init__(self, k, d, assigned_label=None):
        super().__init__(assigned_label=assigned_label)
        self.k=k
        self.d=d

    def toString(self):
        return super().toString()+"LOAD "+str(self.k)+" "+str(self.d)

class add(Instruction):
    def __init__(self, assigned_label=None):
        super().__init__(assigned_label=assigned_label)

    def toString(self): return super().toString()+"ADD"


class sub(Instruction):
    def __init__(self, assigned_label=None):
        super().__init__(assigned_label=assigned_label)

    def toString(self): return super().toString() + "SUB"

class mul(Instruction):
    def __init__(self, assigned_label=None):
        super().__init__(assigned_label=assigned_label)

    def toString(self): return super().toString() + "MUL"

class div(Instruction):
    def __init__(self, assigned_label=None):
        super().__init__(assigned_label=assigned_label)

    def toString(self): return super().toString() + "DIV"

class lt(Instruction):
    def __init__(self, assigned_label=None):
        super().__init__(assigned_label=assigned_label)

    def toString(self): return super().toString() + "LT"

class gt(Instruction):
    def __init__(self, assigned_label=None):
        super().__init__(assigned_label=assigned_label)

    def toString(self): return super().toString() + "GT"

class eq(Instruction):
    def __init__(self, assigned_label=None):
        super().__init__(assigned_label=assigned_label)

    def toString(self): return super().toString() + "EQ"

class neq(Instruction):
    def __init__(self, assigned_label=None):
        super().__init__(assigned_label=assigned_label)

    def toString(self): return super().toString() + "NEQ"

class goto(Instruction):
    def __init__(self, label, assigned_label=None):
        super().__init__(assigned_label=assigned_label)
        self.label=label

    def toString(self):
        return super().toString() + "GOTO "+self.label.toString()

class ifzero(Instruction):
    def __init__(self, label, assigned_label=None):
        super().__init__(assigned_label=assigned_label)
        self.label=label

    def toString(self):
        return super().toString() + "IFZERO "+self.label.toString()

class invoke(Instruction):
    def __init__(self,n,label,d, assigned_label=None):
        super().__init__(assigned_label=assigned_label)
        self.n=n
        self.label=label
        self.d=d

    def toString(self):
        return super().toString() \
               + "INVOKE "+str(self.n)+" "+self.label.toString()+" "+str(self.d)

class ireturn(Instruction):
    def __init__(self, assigned_label=None):
        super().__init__(assigned_label=assigned_label)

    def toString(self): return super().toString() + "RETURN"
    
