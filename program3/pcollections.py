#Submitter: jisook5(Kim, Jisoo)
#Partner: fujs(Fu, Justin)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import re, traceback, keyword

def pnamedtuple(type_name, field_names, mutable=False):
    def show_listing(s):
        for i, l in enumerate(s.split('\n'),1):
            print('{num: >3} {txt}'.format(num = i, txt = l.rstrip()))
            
    legal_name = re.compile('^([a-zA-Z])(\w*)$')
    tn_check = legal_name.match(str(type_name))
    field_names_list = []
    if tn_check == None:
        raise SyntaxError("An illegal name is present in type_name")
    elif type(field_names) == list:
        field_names_list=field_names
        fn_check = [legal_name.match(x) for x in field_names]
    elif type(field_names) == str:
        if ',' in field_names:
            fn_check = [x.strip() for x in field_names.split(',')]
            field_names_list.extend(fn_check)
            for  x in fn_check:
                if x in keyword.kwlist:
                    raise SyntaxError("An illegal name is present in field_names")
                elif legal_name.match(x.strip(' ')) == None:
                    raise SyntaxError("An illegal name is present in field_names")
        else:
            fn_check= field_names.split(' ')
            field_names_list.extend(fn_check)
            for x in fn_check:
                if x in keyword.kwlist:
                    raise SyntaxError("An illegal name is present in field_names")
                elif legal_name.match(x) == None:
                    raise SyntaxError("An illegal name is present in field_names")
    else:
        raise SyntaxError("type_name/field_names is the incorrect type")
    class_template = '''\
class {type_name}:
'''

    def gen_init(field_names_list, mutable):
        result = '''\
    def __init__(self, {fn}, mutable = {m}):
{var}
        self._fields = {fnl}
        self._mutable = {mutable}
        '''
        inner_var = ''
        for each in field_names_list:
            inner_var += ('        self.{x} = {x}\n'.format(x=each))
        return result.format(fn = str(field_names_list).replace('[', ']').replace("'", '').strip(']'),
                            m = mutable,
                            var = inner_var,
                            fnl = field_names_list,
                            mutable = mutable) 
        
    def gen_repr(type_name, field_names_list):
        inner = ''
        inner_format = ''
        for each in field_names_list:
            inner += ('{each1}={each2},'.format(each1=each, each2 = '{'+each+'}'))
            inner_format+=('{each}=self.{each},'.format(each = each))
            
        result = '''\n
    def __repr__(self):
        return '{tn}({inner})'.format({i_f})'''
        return result.format(tn=type_name, inner = inner.strip(','), i_f = inner_format.strip(','))
    
    def gen_get(field_names_list):
        result = ''
        for each in field_names_list:
            x='''\n 
    def get_{each}(self):
        return self.{each}'''
            result += x.format(each=each)
        return result
    
    def gen_getitem():
        inner = "'self.get_{x}()'.format(x = self._fields[index])"
        inner2 = "'self.{x}'.format(x = index)"
        error = "'Entered index '+str(index)+' is out of bounds or is not a name in the field.'"
        result = '''\n
    def __getitem__(self, index):
        if type(index) == int and -1<index<len(self._fields):
            string = ({inner})
            return eval(string)
        if type(index) == str and index in self._fields:
            string = ({inner2})
            return eval(string)
        else:
            raise IndexError({error})
            '''
        return result.format(inner = inner, inner2 = inner2, error = error)
    
    def gen_eq():
        result = '''\n
    def __eq__(self, right):
        if type(self) == type(right):
            right_list = [right[x] for x in range(len(right._fields))]
            left_list = [self[x] for x in range(len(self._fields))]
            return left_list == right_list
        else:
            return False'''
        return result
    
    def gen_replace(type_name, field_names, mutable):
        result = '''\n
    def _replace(self, **kargs):
        if self._mutable and set(kargs.keys()) <= set(self.__dict__.keys()):
            for key, value in kargs.items():
                self.__dict__[key] = value
            return
        elif self._mutable == False and set(kargs.keys()) <=  set(self.__dict__.keys()):
            new_dict = self.__dict__.copy()
            for key, value in kargs.items():
                new_dict[key] = value
{esv}
            return {return_var}
        else:
            raise TypeError('Entered arguments are not values that are in the existing fields')
        '''
        esv = ''
        esv2 = ''
        for each in field_names:
            esv += "            {} = new_dict['{}']\n".format(each, each)
            esv2 += "{},".format(each)
            return_var = "{}({}{})".format(type_name, esv2, mutable)
        return result.format(esv = esv, return_var = return_var)
    
    
  
    class_definition = class_template.format(type_name = type_name) + \
    gen_init(field_names_list, mutable) + \
    gen_repr(type_name, field_names_list) + \
    gen_get(field_names_list) + \
    gen_getitem() + \
    gen_eq() + \
    gen_replace(type_name, field_names_list, mutable)


    # bind class_definition (used below) to the string constructed for the class



    # For initial debugging, always show the source code of the class
    #show_listing(class_definition)
    
    # Execute the class_definition string in a local namespace and bind the
    #   name source_code in its dictionary to the class_defintion; return the
    #   class object created; if there is a syntax error, list the class and
    #   show the error
    name_space = dict(__name__='pnamedtuple_{type_name}'.format(type_name=type_name))
    try:
        exec(class_definition, name_space)
        name_space[type_name].source_code = class_definition
    except(SyntaxError, TypeError):
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]


    
if __name__ == '__main__':
#     Triple1    = pnamedtuple('Triple1', 'a b c')
#     t1 = Triple1(1, 2, 3)
#     t1._replace(a=8, b=9)
#     print(t1)


    
    import driver
    driver.driver()
