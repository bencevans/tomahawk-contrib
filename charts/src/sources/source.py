# Copyright (C) 2011 Casey Link <unnamedrambler@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

class Source(object):
    """
    ABC for sources
    """

    def chart_list(self):
        """
        Return a list of tuples to charts
        (url, display_name)
        """
        raise NotImplementedError("Can't instantiate ABC")

    def get_chart(self, url):
        """
        Return the contents of the chart specified by the url
        """
        raise NotImplementedError("Can't instantiate ABC")
