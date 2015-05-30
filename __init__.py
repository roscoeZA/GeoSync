"""
/***************************************************************************
Name			 	 : GeoSync Plugin
Description          : Simplifies geogig workflow.
Date                 : 25/May/15 
copyright            : (C) 2015 by Roscoe Lawrence
email                : roscoelawrence@gmail.com 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
def name(): 
  return "GeoSync Plugin" 
def description():
  return "Simplifies geogig workflow."
def version(): 
  return "Version 0.1" 
def qgisMinimumVersion():
  return "1.0"
def classFactory(iface): 
  # load GeoSync class from file GeoSync
  from GeoSync import GeoSync 
  return GeoSync(iface)
