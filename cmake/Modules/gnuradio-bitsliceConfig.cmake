find_package(PkgConfig)

PKG_CHECK_MODULES(PC_GR_BITSLICE gnuradio-bitslice)

FIND_PATH(
    GR_BITSLICE_INCLUDE_DIRS
    NAMES gnuradio/bitslice/api.h
    HINTS $ENV{BITSLICE_DIR}/include
        ${PC_BITSLICE_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GR_BITSLICE_LIBRARIES
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

include("${CMAKE_CURRENT_LIST_DIR}/gnuradio-bitsliceTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GR_BITSLICE DEFAULT_MSG GR_BITSLICE_LIBRARIES GR_BITSLICE_INCLUDE_DIRS)
MARK_AS_ADVANCED(GR_BITSLICE_LIBRARIES GR_BITSLICE_INCLUDE_DIRS)
