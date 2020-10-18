// -----------------------------------------------------------------------------
// APP NAME AND VERSION
// -----------------------------------------------------------------------------

#pragma once

#define BUILD_MAIN              "1.15.0"

#define APP_NAME                "ESPURNA"
#ifdef BUILD_ID
#define APP_VERSION             BUILD_MAIN ## "-dev" ## BUILD_ID
#else
#define APP_VERSION             BUILD_MAIN
#endif
#define APP_AUTHOR              "xose.perez@gmail.com"
#define APP_WEBSITE             "http://tinkerman.cat"
#define CFG_VERSION             5
