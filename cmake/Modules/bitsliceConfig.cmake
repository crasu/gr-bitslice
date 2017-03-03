INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_BITSLICE bitslice)

FIND_PATH(
    BITSLICE_INCLUDE_DIRS
    NAMES bitslice/api.h
    HINTS $ENV{BITSLICE_DIR}/include
        ${PC_BITSLICE_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    BITSLICE_LIBRARIES
    NAMES gnuradio-bitslice
    HINTS $ENV{BITSLICE_DIR}/lib
        ${PC_BITSLICE_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(BITSLICE DEFAULT_MSG BITSLICE_LIBRARIES BITSLICE_INCLUDE_DIRS)
MARK_AS_ADVANCED(BITSLICE_LIBRARIES BITSLICE_INCLUDE_DIRS)

