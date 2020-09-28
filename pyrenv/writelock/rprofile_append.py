"""
  Build a string containing only valid R 
  code, to be appended to a project's 
  .Rprofile.

  As it is the goal of this project, this will
  enable using a virtualenv created via poetry
  to be used within RStudio's reticulate package.
"""


def enforce_toml_install() -> str:
    """ in R : check if the package 'RcppTOML'
    has been installed. If not, enforce its installation.
    """
    return """if("RcppTOML" %in% rownames(installed.packages()) == FALSE){ 
    install.packages("RcppTOML")\n}"""


if __name__ == "__main__":
    print(enforce_toml_install())
    print(
      list(filter(lambda x: False if x[0:2] == "__" else x, 
             globals().keys()
      ))
    )
