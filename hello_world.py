from test_module.module import MyClass

def main():
    thing = MyClass("thinger")
    #thing.cleanDataExample()
    thing.StandardScalerExample()
    thing.MinMaxScalaerExample()

if __name__ == "__main__":
    main()