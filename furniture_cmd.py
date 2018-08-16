#import rhinoscript.userinterface
#import rhinoscript.geometry
global rs, rhino

import rhinoscriptsyntax as rs
import Rhino as rhino

__commandname__ = "furniture"

# RunCommand is the called when the user enters the command name in Rhino.
# The command name is defined by the filname minus "_cmd.py"
def RunCommand( is_interactive ):
    #import rhinoscriptsyntax as rs
    
    # Generates simply 2d & 3D rectangular furniture elments
    # Generates simply 2d & 3D rectangular furniture elments
    # 
    # GNU GENERAL PUBLIC LICENSE Version 3
    #
    # by Joern Rettweiler, 2018 august 16
    #
    #
    # Tested with Rhino 5 
    #
    # NO WARRANTY
    #
    # Note: If you want to create a rhino command that you can call via command promt
    # look here: https://developer.rhino3d.com/guides/rhinopython/creating-rhino-commands-using-python/
 

    #import rhinoscriptsyntax as rs
    #import Rhino as rhino

    
    
    
    def ac_furniture():
        global geom_functionarea, geom_workarea, geom2d, group3d, obj, obj2d_function
      
        group3d = "geom3d"
        rs.AddGroup(group3d)
        
        
        obj2d_function = []
     
      
      
      
      
        #############################
        ##FUNCTION DEFINITIONS BEGIN##
        ##############################
      
      
      
      
      
        def ac_layercreation():
            
            global layer_furniture, layer_geom2d, layer_geom3d, layer_workarea, layer_text, layer_functionarea, layer_furniture_color, layer_geom2d_color, layer_geom3d_color, layer_workarea_color, layer_functionarea_color, layer_text_color, layer_geom3d_pro
            
            #Parent layer
            layer_furniture = ("Furniture")
            layer_furniture_color = [0,0,0]
        
            #Enter / Edit Here your furniture layer names EDIT ONLY VALUES IN PARANTHESES,
            #default :2 geom Color red = [255,0,0]
            layer_geom2d = ("AC-Geom2d")
            layer_geom2d_color = [255,0,0]
        
            #default :3D geom Colorwhite = [255,255,255]
            layer_geom3d = ("AC-Geom3d")
            layer_geom3d_color = [255,255,255]
            
            #default :3D geom Colorwhite = [190,190,190]
            layer_geom3d_pro = ("AC-Geom3d_projection")
            layer_geom3d_projection_color = [190,190,190]
            
            #default : workarea Color blue = [0,255,255]
            layer_workarea = ("AC-Working_area")
            layer_workarea_color = [0,255,255]
            
            #default : workarea Color blue = [0,255,255]
            layer_functionarea = ("AC-Function_area")
            layer_functionarea_color = [0,255,255]
        
            #default : Text Color blue = [0,0,0]
            layer_text = ("AC-Text")
            layer_text_color = [0,0,0]
        
        
    
        
        
    
            
            #Add layer after previous operation are succesfull
            rs.AddLayer(layer_furniture, layer_furniture_color)
            
            rs.AddLayer(layer_geom2d, layer_geom2d_color, parent=layer_furniture)
            
            rs.AddLayer(layer_geom3d, layer_geom3d_color, parent=layer_furniture)
            
            rs.AddLayer(layer_workarea, layer_workarea_color, parent=layer_furniture)
            rs.LayerLinetype(layer_workarea, linetype="Dashed")
            
            rs.AddLayer(layer_text, layer_text_color, parent=layer_furniture)
            
            rs.AddLayer(layer_geom3d_pro, layer_geom3d_projection_color, parent=layer_furniture)
            rs.LayerLinetype(layer_geom3d_pro, linetype="Dashed")
            
            rs.AddLayer(layer_functionarea, layer_functionarea_color, parent=layer_furniture)
            rs.LayerLinetype(layer_functionarea, linetype="Dashed")
            
            rs.CurrentLayer(layer_furniture)
        
        
        def ac_geom2d(width, depth):
            global geom_text, geom2d, blockname, basepoint
            
            rs.CurrentLayer(layer_geom2d)
            planexy = rs.WorldXYPlane()
            geom2d = rs.AddRectangle(planexy, width, depth)
            
            
            
            geom2d_centroid = rs.CurveAreaCentroid(geom2d)
            
            basepoint = geom2d_centroid[1]
            #rs.AddPoint((geom2d_centroid))
            
            #info text
            if furniture_typ == 4:
                textdottext = (furniture_name + "\n" 
                + str(furniture_width_cm)+ " x " + str(furniture_depth_cm))
            elif furniture_typ == 5:
                textdottext = (furniture_name + "\n" 
                + str(furniture_width_cm)+ " x " + str(furniture_depth_cm))
            elif furniture_typ == 9:
                
                if furniture_width_cm <= 120:
                    sittings = 1
                    people = " Seat"
                else:
                    sittings = furniture_width_cm // 60
                    people = " Seats"
                
                textdottext = (furniture_name + "\n" 
                + str(furniture_width_cm)+ " x " + str(furniture_depth_cm) + "\n" + str(sittings)+ people)
                
            elif furniture_typ == 10:
                
                
                if furniture_width_cm <= 120:
                    divan_bed = "1" 
                    people = " person bed"
                else:
                    divan_bed = "2" 
                    people = " persons bed"
                    
                
                textdottext = (furniture_name + "\n"
                + str(furniture_width_cm)+ " x " + str(furniture_depth_cm) + "\n" + str(divan_bed)+ people)
            
            
            else:
                
                #Generate folder height 
                #DOPPLE CHECK THIS VALUE EXIST ALSO AT function ac_geom3d_shelf_cabinet!!!
                shelf_distance = 350
                shelf_count = furniture_hight / shelf_distance
                shelf_count = shelf_count -1.5
                shelf_count = int(round(shelf_count))
                shelf_count = shelf_count + 1
                
                #FH = folder heigth
                textdottext = (furniture_name + "\n" 
                + str(furniture_width_cm)+ " x " + str(furniture_depth_cm) + "\n" + str(furniture_hight_cm)+ " cm = "
                + str(shelf_count) + " FH")
                
    
            
            
            rs.CurrentLayer(layer_text)
            geom_text = rs.AddTextDot(textdottext, geom2d_centroid[0])
            #rhino.text
            #Generate Blockname
            blockname = (str(furniture_name) + str(furniture_width_cm) + "x" + str(furniture_depth_cm))
            
            
            
            
            
            
        def ac_geom2d_workarea(width):
            global geom_workarea, geom_functionarea
            
            planexy_wa = rs.WorldXYPlane()
            
            
            # Reference (2018 august 08) https://www.baua.de/DE/Angebote/Rechtstexte-und-Technische-Regeln/Regelwerk/ASR/pdf/ASR-A1-2.pdf?__blob=publicationFile&v=7
            depth_workarea = -1000
            rs.CurrentLayer(layer_workarea)
            geom_workarea = rs.AddRectangle(planexy_wa, width, depth_workarea)
            
            
            geom_functionarea = geom_workarea
        
        def ac_geom2d_functionarea(width, depth):
            global geom_functionarea, geom_workarea
            
            planexy_wa = rs.WorldXYPlane()
            
            
            # Reference (2018 august 08) https://www.baua.de/DE/Angebote/Rechtstexte-und-Technische-Regeln/Regelwerk/ASR/pdf/ASR-A1-2.pdf?__blob=publicationFile&v=7
            depth = depth * -1 
            rs.CurrentLayer(layer_functionarea)
            geom_functionarea = rs.AddRectangle(planexy_wa, width, depth)
            
            geom_workarea = geom_functionarea
        
        
        def ac_geom3d_table():
            
            global table_foot_3d, geom3d
            rs.CurrentLayer(layer_geom3d_pro)
            
            side_dist = 50 #distance to side
            
            #Table foot base bottom left
            table_pt_1 = (side_dist,side_dist,0)
            foot_1 = rs.AddRectangle(table_pt_1,side_dist,side_dist)
            
            #Table foot base bottom rigth
            table_pt2_x = furniture_width - (side_dist * 2)
            table_pt_2 = (table_pt2_x,side_dist,0)
            foot_2 = rs.AddRectangle(table_pt_2,side_dist,side_dist)
            
            #Table foot base Top right
            table_pt3_y = furniture_depth - (side_dist * 2)
            table_pt_3 = (table_pt2_x, table_pt3_y,0)
            foot_3 = rs.AddRectangle(table_pt_3,side_dist,side_dist)
            
            #Table foot base Top left
            table_pt_4 = (side_dist, table_pt3_y, 0)
            foot_4 = rs.AddRectangle(table_pt_4,side_dist,side_dist)
            
            #add foots to array
            table_foot_2d = [foot_1, foot_2, foot_3, foot_4]
            
            #Extrude 2d foot geometry and put then into array/list
            rs.CurrentLayer(layer_geom3d)
            loop_count = 0
            table_foot_3d = []
            while loop_count < len(table_foot_2d):
                
                table_foot = rs.ExtrudeCurveStraight(table_foot_2d[loop_count], (0,0,0),(0,0,furniture_hight))
                rs.CapPlanarHoles(table_foot)
                table_foot_3d.append(table_foot)
                
                #add material to table-legs
                ac_material_surface(table_foot, "leg")
                
                loop_count = loop_count + 1
                
            #Add table plate
            plane_rectangle_pt = (0, 0, furniture_hight)
            table_table = rs.AddRectangle(plane_rectangle_pt, furniture_width, furniture_depth)
            table_table = rs.ExtrudeCurveStraight(table_table, (0,0,0),(0,0,20))
            rs.CapPlanarHoles(table_table)
            
            
            #add polysurfaces objects to group
            obj = rs.ObjectsByType(16, select=False, state = 0)
            rs.AddObjectsToGroup(obj,group3d)
            
            
            #add material to table surface
            ac_material_surface(table_table, "srf")
        
        def ac_geom3d_desk():
    
            thickness_elements = 50
            
            rs.CurrentLayer(layer_geom3d)
    
            
            def ac_geom3d_desk_foot(base):
                
                if base > 0:
                    base = base - thickness_elements
                #first 2d bow base for extrusion 
                arc_start_pt = (base,furniture_depth,0)
                arc_end_pt = (base, furniture_depth-thickness_elements, thickness_elements)
                arc_pt_on_arc = (base, furniture_depth - thickness_elements*0.34,thickness_elements*0.66)
                arc_1 = rs.AddArc3Pt(arc_start_pt,arc_end_pt,arc_pt_on_arc)
            
                #second 2d bow base for extrusion 
                arc_start_pt2 = (base,0,0)
                arc_end_pt2 = (base, thickness_elements, thickness_elements)
                arc_pt_on_arc2 = (base, thickness_elements*0.34, thickness_elements*0.66)
                arc_2 = rs.AddArc3Pt(arc_start_pt2,arc_end_pt2,arc_pt_on_arc2)
            
                line_1 = rs.AddLine(arc_end_pt,arc_end_pt2)
                line_2 = rs.AddLine(arc_start_pt,arc_start_pt2)
            
                foot_extrude_base = rs.JoinCurves([arc_1, arc_2, line_1, line_2], delete_input=True)
                foot_extruded = rs.ExtrudeCurveStraight(foot_extrude_base, (base,0,0),(base+thickness_elements,0,0))
                foot_extruded = rs.CapPlanarHoles(foot_extruded)
                
                #add cylinder
                base = (base + thickness_elements/2, furniture_depth/2, thickness_elements)
                hight = furniture_hight - thickness_elements
                radius = thickness_elements / 2 
                cylinderfoot =rs.AddCylinder(base, hight, radius, cap=True)
                
                #add material to elements
                ac_material_surface(cylinderfoot, "leg")
                
            ac_geom3d_desk_foot(0)
            ac_geom3d_desk_foot(furniture_width)
            
            #Add table plate
            plane_rectangle_pt = (0, 0, furniture_hight)
            table_table = rs.AddRectangle(plane_rectangle_pt, furniture_width, furniture_depth)
            table_table = rs.ExtrudeCurveStraight(table_table, (0,0,0),(0,0,20))
            
            rs.CapPlanarHoles(table_table)
            
            
            
            #Add Material Color
            ac_material_surface(table_table, "srf")
            
            
            #add polysurfaces objects to group
            obj = rs.ObjectsByType(16, select=False, state = 0)
            rs.AddObjectsToGroup(obj,group3d)
            
            
        def ac_geom3d_shelf_cabinet(bottomhight):
            global shelf_objects
            
            
            wallthickness = 20
            
            
            
            rs.CurrentLayer(layer_geom3d)
            
            
            
            
            
            def ac_geom3d_shelf_cabinet_sidewall(base):
                global sw
                
                if base > 0:
                    base = base - wallthickness
                
                sw_pt1 = (base,0,0)
                
                #Sidewall
                
                sw = rs.AddRectangle(sw_pt1, wallthickness,  furniture_depth)
                
                sw = rs.ExtrudeCurveStraight(sw, (0,0,0), (0,0,(furniture_hight- wallthickness)))
                rs.CapPlanarHoles(sw)
                
                #add material 
                ac_material_surface(sw, "srf")
            
            def ac_geom3d_shelf_cabinet_inside():
                
                #bottom 
                #attention 50 is hardocded value for bottom standing furniture!
                shelf_depth = furniture_depth - 2 * wallthickness
                
                if bottomhight == 50:
                    base = (wallthickness, wallthickness, bottomhight)
                    basetarget = (wallthickness,wallthickness,0)
                    
                    #shelf_depth = furniture_depth - 2 * wallthickness
                    
                    
                else:
                    base = (wallthickness, 0, bottomhight)
                    basetarget = (wallthickness, 0,0)
                    
                    #shelf_depth = furniture_depth - 2 * wallthickness
                
                shelf_width = furniture_width - 2 * wallthickness
                #shelf_depth = furniture_depth - 2 * wallthickness
                bottom_shelf = rs.AddRectangle(base,shelf_width, shelf_depth)
                bottom_shelf = rs.ExtrudeCurveStraight(bottom_shelf, base, basetarget)
                rs.CapPlanarHoles(bottom_shelf)
                
                #Add material to obj
                ac_material_surface(bottom_shelf, "srf")
                
                if furniture_hight >= 700:
                    shelf_distance = 350 + wallthickness
                    shelf_count = furniture_hight / shelf_distance
                    
                    #start posistion -> 50=bottomhight for distance between bottom shelf
                    shelf_position = shelf_distance + bottomhight
                    
                    print "shelf Count"
                    print shelf_count
                    #round up
                    shelf_count = shelf_count -1.5
                    print "shelf Count"
                    print shelf_count
                    
                    
                    loopbreaker = 0
                    while loopbreaker < shelf_count:
                        
                        base = (wallthickness, wallthickness, shelf_position)
                        
                        shelf = rs.AddRectangle(base,shelf_width, shelf_depth)
                        
                        
                        #
                        base_extrude_target = (wallthickness, wallthickness, (shelf_position + wallthickness))
                        shelf = rs.ExtrudeCurveStraight(shelf, base, base_extrude_target)
                        
                        rs.CapPlanarHoles(shelf)
                        
                        
                        
                        
                        shelf_position = shelf_position + shelf_distance
                        
                        loopbreaker = loopbreaker + 1
                        
                        #add material
                        ac_material_surface(shelf, "srf")
            
            #back wall
            bw_pt = (wallthickness, furniture_depth, 0)
            bw_width = furniture_width - 2* wallthickness
                    
            bw =rs.AddRectangle(bw_pt, bw_width, (wallthickness * -1))
            bw = rs.ExtrudeCurveStraight(bw, (0,0,0), (0,0,(furniture_hight- wallthickness)))
            rs.CapPlanarHoles(bw)
            
            #add material to object back
            ac_material_surface(bw, "srf")
    
            
            #top
            tw_pt = (0,0,(furniture_hight- wallthickness))
            tw_pt_target = (0,0, furniture_hight)
            tw = rs.AddRectangle(tw_pt, furniture_width, furniture_depth)
            tw = rs.ExtrudeCurveStraight(tw, tw_pt, tw_pt_target)
            rs.CapPlanarHoles(tw)
            
            #add material to object top
            ac_material_surface(tw, "srf")
            
            #Execute Functions
            ac_geom3d_shelf_cabinet_sidewall(0)
    
            
            ac_geom3d_shelf_cabinet_sidewall(furniture_width)
    
            
            ac_geom3d_shelf_cabinet_inside()
            
            
            #add polysurfaces objects to group
            obj = rs.ObjectsByType(16, select=False, state = 0)
            geom3d = rs.AddObjectsToGroup(obj,group3d)
            
            
            
            
            
        def ac_geom3d_wing_door():
            
            
            wallthickness = 20
            door_width = furniture_width / 2 - wallthickness
            
            #adjust door extrusion start point do avoid gaps
            if furniture_typ == 1:
                overlapping_door = 50 - 20
            else:
                overlapping_door = 50 - 30
            
            
            
            
            def ac_geom3d_wing_door_itself(base):
                rotate = "flase"
                
                
                
                base_ogirinal = base
                if base > 0:
                    base = base / 2 - wallthickness
                    rotate = "true"
                
                wdpt = (base + wallthickness, 0, overlapping_door)
                wdtarget_hight = (furniture_hight - wallthickness)
                wdtarget = (base + wallthickness,0,wdtarget_hight)
                door1 = rs.AddRectangle(wdpt, door_width, wallthickness)
                door1 = rs.ExtrudeCurveStraight(door1, wdpt, wdtarget)
                
                
                if rotate == "true":
                    wdp2 = (base_ogirinal - wallthickness, 0, 30)
                    rs.RotateObject(door1,wdp2,30,None, copy=False)
                
                
                rs.CapPlanarHoles(door1)
                
                #add material to object
                ac_material_surface(door1, "srf")
                
                
            def ac_geom2d_wing_door(base):
                global  obj2d_function
                
                rs.CurrentLayer(layer_functionarea)
                start_y_distance = (-1 * furniture_depth)
                startpt = ((furniture_width / 2), 0 ,0)
                endpt = (wallthickness,start_y_distance,0)
                
                point_on_arc_x = (furniture_width / 2) * +0.90
                point_on_arc_y = furniture_depth * -0.33
                point_on_arc = (point_on_arc_x, point_on_arc_y, 0)
                
                line =rs.AddLine(endpt, (wallthickness,0,0))
                
                arc = rs.AddArc3Pt(endpt, startpt,point_on_arc)
                opening_projection1 = rs.JoinCurves([line,arc], delete_input=True)
                
                opening_projection2 = rs.MirrorObject(opening_projection1, ((furniture_width /2),0,0), ((furniture_width /2),wallthickness,0),copy=True)
                
                
                obj2d_function = [opening_projection2,opening_projection1]
                
                
                
                
            
            
            ac_geom3d_wing_door_itself(0)
            ac_geom3d_wing_door_itself(furniture_width)
            
            ac_geom2d_wing_door(0)
            
            
    
    
        def ac_lock_prevlayer():
            
            
            layername = rs.LayerNames()
            
            print "layerbane"
            print layername[1]
            print len(layername)
            loopbreaker = 0
            
            
            
            while loopbreaker < len(layername):
                rs.LayerLocked(layername[loopbreaker], locked=True)
                loopbreaker = loopbreaker + 1
                print "loop"
                print loopbreaker
    
        def ac_geom3d_sideboard_door():
            
            
            if furniture_typ == 3:
                overlapping_door = 50 - 20 
                correctvalue = 10
            else:
                overlapping_door = 50 - 30
                correctvalue = 0
            
            wallthickness = 20
            wallthickness = wallthickness / 2
            base = furniture_width / 2 - wallthickness
            
            wdpt = (wallthickness, 0, overlapping_door)
            wdtarget_hight = (furniture_hight - overlapping_door + correctvalue)
            wdtarget = (wallthickness,0,wdtarget_hight)
            door1 = rs.AddRectangle(wdpt, base, wallthickness)
            door1 = rs.ExtrudeCurveStraight(door1, wdpt, wdtarget)
            
            rs.CapPlanarHoles(door1)
            
            base2 = furniture_width / 2
            wdpt2 = (base2, wallthickness, overlapping_door )
            wdpt2_target = (base2, wallthickness, wdtarget_hight )
            width_slided_door = furniture_width / 4
            door2 = rs.AddRectangle(wdpt2, width_slided_door, wallthickness)
            door2 = rs.ExtrudeCurveStraight(door2, wdpt2, wdpt2_target)
            rs.CapPlanarHoles(door2)
            
            #add material to objects
            ac_material_surface(door1, "srf")
            ac_material_surface(door2, "srf")
            
            
            def ac_geom_2d_sideboard_arrow():
                
                
                wallthickness = 20
                #arrow_distance = 100
                arrow_width = 25
                
                rs.LayerLocked(layer_geom2d, locked = False)
                rs.CurrentLayer(layer_geom2d)
                
                
                
                def geom_2d_sideboard_arrow_arrow(arrow_distance, mirror):
                    global obj2d_function, opening_projection3, opening_projection4
                    
                    
                    
                    
                    #upper point
                    arrow_pt1y = -arrow_distance + arrow_width
                    arrow_pt1 = (150, arrow_pt1y, 0)
                
                    #lower point
                    arrow_pt2y = -arrow_distance - arrow_width
                    arrow_pt2 = (150, arrow_pt2y, 0)
                
                    #arrow point
                    arrow_pt3 = (80, -arrow_distance, 0)
                
                    opening_projection1 = rs.AddPolyline((arrow_pt1, arrow_pt2, arrow_pt3, arrow_pt1))
                
                
                    arrowline_pt1 = (150, -arrow_distance, 0)
                    arrowline_pt2x = furniture_width * 0.7
                    arrowline_pt2 = (arrowline_pt2x, -arrow_distance, 0)
                    opening_projection2 = rs.AddLine(arrowline_pt1, arrowline_pt2)
                    
                    arrow = (opening_projection1, opening_projection2)
                    
                    #mirror for 2nd run 1 = true
                    if mirror == 1:
                        mirrorpt_width = furniture_width / 2
                        mirror_pt1 = (mirrorpt_width, 0, 0)
                        mirror_pt2 = (mirrorpt_width, 100, 0)
                        arrow2 = rs.MirrorObject(arrow, mirror_pt1, mirror_pt2, copy=False)
                        
                        opening_projection1 = opening_projection1
                        opening_projection2 = opening_projection2
                        
                        obj2d_function = [opening_projection1, opening_projection2, opening_projection3, opening_projection4]
                        
                        
                        
                    else:
                        arrow1 = (opening_projection1, opening_projection2)
                        opening_projection3 = opening_projection1
                        opening_projection4 = opening_projection2
                        
                
                geom_2d_sideboard_arrow_arrow(100, 0)
                geom_2d_sideboard_arrow_arrow(150, 1)
                
                
                
                
                
                rs.LayerLocked(layer_geom2d, locked = True)
                
            ac_geom_2d_sideboard_arrow()
            
    
        def ac_branding():
            global branding
            pt = (0,10,0)
            
            author = "Joern Rettweiler \n 2018 august"
            branding = rs.AddText(author,pt, height=1)
            
        
        def ac_material_surface(mat2obj, element):
            #Add Material Color, edit rgb values if you want another colors
            
            if element == "srf":
                material_color = (255,245, 215)
            elif element == "leg":
                material_color = (230,230,230)
            elif element == "textile":
                material_color = (255,255,255)
            
            index_material = rs.AddMaterialToObject(mat2obj)
            
            mcolor = rs.MaterialColor(index_material, material_color) #ahorn
            print "mcolor:"
            print mcolor
    
    
            rs.MaterialName(index_material, "Furniture_Surface")
        
            print "indexmateri"
            print index_material
            
        def ac_geom_2d_sofa():
            global geom_functionarea, geom_workarea, obj2d_function
            
            width_armrest = 100
            armrest_height = 600
            seating_height = 400
            backrest_height = 800
            
            base_armrest2x = furniture_width - width_armrest
            base_backresty = furniture_depth - width_armrest
            seating_width = furniture_width - 2 * width_armrest
            seating_depth = furniture_depth - width_armrest
            
            rs.CurrentLayer(layer_geom2d)
            
            base_armrest1 = (0,0,0)
            target_armrest1 = (0,0,armrest_height)
            
            base_seating = (width_armrest, 0,0)
            target_seating = (width_armrest, 0, seating_height)
            
            base_armrest2 = (base_armrest2x,0,0)
            target_armrest2 = (base_armrest2x,0,armrest_height)
            
            base_backrest = (width_armrest, base_backresty, 0)
            target_backrest = (width_armrest, base_backresty, backrest_height)
            
            armrest1_2d = rs.AddRectangle(base_armrest1, width_armrest,furniture_depth)
            armrest2_2d = rs.AddRectangle(base_armrest2, width_armrest,furniture_depth)
            seating_2d = rs.AddRectangle(base_seating, seating_width, seating_depth)
            backrest_2d = rs.AddRectangle(base_backrest, seating_width, width_armrest)
            obj2d_function = [armrest1_2d, armrest2_2d, seating_2d, backrest_2d]
            
            
            rs.CurrentLayer(layer_geom3d)
            
            armrest1_3d = rs.ExtrudeCurveStraight(armrest1_2d,base_armrest1,target_armrest1)
            armrest2_3d = rs.ExtrudeCurveStraight(armrest2_2d,base_armrest2,target_armrest2)
            seating_3d = rs.ExtrudeCurveStraight(seating_2d,base_seating,target_seating)
            backrest_3d = rs.ExtrudeCurveStraight(backrest_2d,base_backrest,target_backrest)
            
            rs.CapPlanarHoles(armrest2_3d)
            rs.CapPlanarHoles(armrest1_3d)
            rs.CapPlanarHoles(seating_3d)
            rs.CapPlanarHoles(backrest_3d)
            
    
            
            ac_material_surface(armrest1_3d, "leg")
            ac_material_surface(armrest2_3d, "leg")
            ac_material_surface(seating_3d, "leg")
            ac_material_surface(backrest_3d, "leg")
            
            #some stuff should be removed in future...
            geom2d = backrest_2d
            geom_workarea = geom2d
            geom_functionarea = geom2d
            
        def ac_geom_bed():
            global geom_functionarea, geom_workarea, obj2d_function
    
            bedheight = 250
            legdist = 50
            legs3d = []
            bedthickness = 150
            pillow_height = 150
            
            #decision between normal bed and hospital bed
            if furniture_hight >= 800:
                #hospital
                leg_dim = 50
                bedheight = 700
                
            else:
                #default bed
                leg_dim = 70
                bedheight = 250
            
            basebed = (0,0, bedheight)
            targetheight = bedthickness + bedheight
            targetbed = (0,0,targetheight)
            
            
            #legs
            pt23x = furniture_width - legdist
            pt34y = furniture_depth - legdist
            
            
            basept1 = (legdist,legdist,0)
            targetpt1 = (legdist,legdist,bedheight)
            
            basept2 = (pt23x,legdist,0)
            targetpt2 = (pt23x,legdist,bedheight)
            
            basept3 = (pt23x, pt34y, 0)
            targetpt3 = (pt23x, pt34y, bedheight)
            
            basept4 =(legdist,pt34y, 0)
            targetpt4 = (legdist,pt34y,bedheight)
            
            #pillow
            pillow_width = -furniture_width *0.20
            pillow_depth = furniture_depth - legdist - leg_dim
            targetpillow_z = pillow_height + targetheight
            
            pillowy = legdist
            basepillow = (pt23x, pillowy, targetheight)
            targetpillow = (pt23x, pillowy, targetpillow_z)
                
            geom2d_leg_pts = [basept1, basept2, basept3, basept4]
            geom2d_leg_target_pts = [targetpt1, targetpt2, targetpt3, targetpt4]
            
            #loopbreaker = 0
            #while loopbreaker < len(lengeom2d_leg_pts):
            
            rs.CurrentLayer(layer_geom2d)
            leg1 = rs.AddRectangle(basept1, leg_dim, leg_dim)
            leg2 = rs.AddRectangle(basept2, -leg_dim, leg_dim)
            leg3 = rs.AddRectangle(basept3, -leg_dim, -leg_dim)
            leg4 = rs.AddRectangle(basept4, leg_dim, -leg_dim)
            
            rs.CurrentLayer(layer_geom3d)
            pillow_2d = rs.AddRectangle(basepillow, pillow_width, pillow_depth)
            pillow_3d = rs.ExtrudeCurveStraight(pillow_2d, basepillow, targetpillow)
            rs.DeleteObject(pillow_2d)
            rs.CapPlanarHoles(pillow_3d)
            
            obj2d_function = [leg1, leg2, leg3, leg4]
            
            
            
            #3d geom creation
            
            loop = 0
            while loop < len(obj2d_function):
                leg3d = rs.ExtrudeCurveStraight(obj2d_function[loop],geom2d_leg_pts[loop],geom2d_leg_target_pts[loop])
                legs3d.append(leg3d)
                ac_material_surface(leg3d, "leg")
                
                loop = loop + 1
            print "leng of leg33d"
            print len(legs3d)
            
            bed_2d =rs.AddRectangle(basebed,furniture_width,furniture_depth)
            bed_3d = rs.ExtrudeCurveStraight(bed_2d, basebed, targetbed)
            rs.DeleteObject(bed_2d)
            rs.CapPlanarHoles(bed_3d)
            
            
            #color
            ac_material_surface(pillow_3d, "textile")
            ac_material_surface(bed_3d, "textile")
            #ac_material_surface(leg1, "leg")
            #ac_material_surface(leg2, "leg")
            #ac_material_surface(leg3, "leg")
            #ac_material_surface(leg4, "leg")
            
            
            #some stuff should be removed in future..
            geom2d = leg1
            geom_workarea = geom2d
            geom_functionarea = geom2d
            
            
        #############################
        ##FUNCTION DEFINITIONS END###
        #############################
        
        
        
        
        
        print "UP = Uprigth Section"
        furniture_typ = rs.GetInteger("1=filling cabinet 2=Shelf 3=sideboard 4=table, 5=desk, 6=filling cabinet UP, 7=sideboard UP,8 shelf UP, 9=Sofa]", 5, 0, 10 )
        print furniture_typ
        
        #Get Furniture Dimensions and Scale them to mm
        furniture_width_cm = rs.GetReal("Width of furniture [cm]", 80, 0)
        furniture_width = furniture_width_cm * 10
        furniture_depth_cm = rs.GetReal("Depth of furniture [cm]", 42, 0)
        furniture_depth = furniture_depth_cm * 10
        
            
        
        if furniture_typ == 5:
            furniture_hight = 800
            furniture_hight_cm = furniture_hight / 10
        
        elif furniture_typ == 4:
            furniture_hight = 800
            furniture_hight_cm = furniture_hight / 10
            
            
        else:
            furniture_hight = rs.GetReal("Hight of furniture [cm]", 80, 0)
            #print("Test")
            furniture_hight = furniture_hight *10
            furniture_hight_cm = furniture_hight / 10
    
        ac_layercreation()
        
        ac_lock_prevlayer()
        
        ac_branding()
    
        #Add text to textvariable and execute main functions
        
        #fillin cabinet
        if furniture_typ == 1:
            #filling cabinet furniture like shelf with wing doors
            furniture_name = "filling cabinet"
            ac_geom2d_functionarea(furniture_width, furniture_depth)
            ac_geom3d_shelf_cabinet(50)
            ac_geom3d_wing_door()
        
        #filling cabinet uprigth Section
        elif furniture_typ == 6:
            furniture_name = "filling cabinet UP"
            ac_geom2d_functionarea(furniture_width, furniture_depth)
            ac_geom3d_shelf_cabinet(20)
            ac_geom3d_wing_door()
            
        elif furniture_typ == 2:
            furniture_name = "Shelf"
            ac_geom2d_functionarea(furniture_width, furniture_depth)
            ac_geom3d_shelf_cabinet(50)
        
        elif furniture_typ == 8:
            furniture_name = "Shelf UP"
            ac_geom2d_functionarea(furniture_width, furniture_depth)
            ac_geom3d_shelf_cabinet(20)
        #
        #Sideboards normal & Upright Sections
        #
        elif furniture_typ == 3:
            #sideboard shelf with sliding door
            furniture_name = "Sideboard"
            ac_geom2d_functionarea(furniture_width, furniture_depth)
            
            
            ac_geom3d_shelf_cabinet(50)
            ac_geom3d_sideboard_door()
            
        elif furniture_typ == 7:
            #sideboard shelf with sliding door
            furniture_name = "Sideboard UP"
            ac_geom2d_functionarea(furniture_width, furniture_depth)
            ac_geom3d_shelf_cabinet(20)
            ac_geom3d_sideboard_door()
    
    
    
        elif furniture_typ == 4:
            furniture_name = "Table"
            
            geom_functionarea = rs.AddPoint( (0,0,0) )
            geom_workarea = geom_functionarea
            ac_geom3d_table()
            
        
        elif furniture_typ == 5:
            furniture_name = "Desk"
            ac_geom3d_desk()
            
            rs.AddLayer(layer_text, layer_text_color, parent=layer_furniture)
            ac_geom2d_workarea(furniture_width)
        
        elif furniture_typ == 9:
            furniture_name = "Sofa"
            ac_geom_2d_sofa()
        
        
        elif furniture_typ == 10:
            if furniture_hight < 800:
                furniture_name = "bed"
            else:
                furniture_name = "divan bed"
            
            ac_geom_bed()
        
        #elif furniture_typ == 3:
        #    furniture_name = "XXX"
        
        
        
       
        
        rs.CurrentLayer(layer=layer_geom2d)
        ac_geom2d(furniture_width, furniture_depth)
        
        
        
        rs.CurrentLayer(layer=layer_furniture)
        
        #clean useless geom and lock layers
        #lock partial
        rs.LayerLocked(layer_geom2d, locked = True)
        rs.LayerLocked(layer_geom3d_pro, locked = True)
        rs.LayerLocked(layer_workarea, locked = True)
        rs.LayerLocked(layer_functionarea, locked = True)
        rs.LayerLocked(layer_text, locked = True)
        #clean
        obj_delete = rs.ObjectsByType(4, select=False, state=1)
        rs.DeleteObjects(obj_delete)
        
        #unlock layers
        rs.LayerLocked(layer_geom2d, locked = False)
        rs.LayerLocked(layer_geom3d_pro, locked = False)
        rs.LayerLocked(layer_workarea, locked = False)
        rs.LayerLocked(layer_functionarea, locked = False)
        rs.LayerLocked(layer_text, locked = False)
        
        print "objd function value"
        print len(obj2d_function)
    
        #add all objects curves and polysrf to array/list
        obj3d = rs.ObjectsByType(16, select=False, state = 1)
        blockobj = [geom_text,geom2d, geom_workarea, geom_functionarea]
        blockobj.extend(obj3d)
        blockobj.extend(obj2d_function)
        blockobj.append(branding)
        
    
        
        
        rs.CurrentLayer(layer_furniture)
        rs.AddBlock(blockobj, basepoint, blockname, delete_input=True)
        rs.InsertBlock(blockname, basepoint)
            
            
            
            
            
            
    
    
    
    
    #call function
    ac_furniture()




  # you can optionally return a value from this function
  # to signify command result. Return values that make
  # sense are
  #   0 == success
  #   1 == cancel
  # If this function does not return a value, success is assumed
    return 0
RunCommand(True)

