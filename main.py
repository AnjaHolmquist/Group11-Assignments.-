import ifcopenshell
import bpy
from blenderbim.bim.ifc import IfcStore
file = IfcStore.get_file()
walls = file.by_type("IfcWallStandardCase")

wall = model.by_type('IfcWall')
len(wall)

for wall in walls:
    print(wall.Name)
    
for wall in walls:
    print(wall.id)
    
Print(Walls)
walls[0]
walls[19]

for wall in walls:
    print(wall.Name)
    
    ## get property sets attached to beams through IsDefinedBy"
    for definition in wall.IsDefinedBy:
        
        ## To support IFC2X3, we need to filter our results.
        if definition.is_a('IfcRelDefinesByProperties'):
            property_set = definition.RelatingPropertyDefinition
            
            
            ## Sort by the name of the propertySet
            if property_set.Name == "PSet_Revit_Dimensions":
               for property in property_set.HasProperties:
                    
                    #print(property)
                    ## sort b the name of the property
                    if property.Name == "Volume":
                        print(wall.Name)
                        print(property.NominalValue.wrappedValue)
