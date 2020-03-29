#!/usr/bin/env python

##mp port=8080 to avoid comflict with Splunk

if __name__ == '__main__':
    from mhn import mhn
    mhn.run(debug=False, host='0.0.0.0', port=8080)
