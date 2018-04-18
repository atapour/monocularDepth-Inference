def create_model(args):
    model = None
    from .test_model import TestModel
    model = TestModel()
    model.initialize(args)
    print("The model has been created")
    return model
