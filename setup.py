modules = set(['os','sys','boto'])

for module in modules:
      try:
            __import__(module)
      except ImportError:
            print module + " does not exist."
            raise
                        
