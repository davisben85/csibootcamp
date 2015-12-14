modules = set(['pip'])

for module in modules:
      try:
            __import__(module)
      except ImportError:
            print module + " exists."
                        
