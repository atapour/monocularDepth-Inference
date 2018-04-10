def create_model(args):
    model = None
    from .test_model import TestModel
    model = TestModel()
    model.initialize(args)
    print("the inference model was created")
    return model
