from anuga_bmi import BmiAnuga

cfg = """
domain_type: outline
boundary_filename: outline.csv
elevation_filename: raster.asc
projection_filename: raster.prj
output_filename: anuga_output
output_timestep: 10
boundary_tags: {'bottom':[0],'side1':[1],'side2':[2],'top':[3],'side3':[4],'side4':[5]}
boundary_conditions: {'bottom':['Dirichlet', 1510, 0, 0],'side1':'Reflective','side2':'Reflective','top':['Dirichlet',1528, 0., 0.],'side3':'Reflective','side4':'Reflective'}
maximum_triangle_area: 10.0
initial_flow_depth: 0.0
interior_polygon_filename: inner_boundary.csv
interior_polygon_triangle_area: 10.0
toggle_sediment_transport: False
inflow_sediment_concentration: 0.0
initial_sediment_concentration: 0.0
toggle_vegetation_drag: False
vegetation_stem_diameter: 0.0
vegetation_stem_spacing: 0.0
Mannings_n_parameter: 0.0
"""

with open('anuga.yaml', 'w') as fp:
    fp.write(cfg)

model = BmiAnuga()
print model.get_component_name()
# model.initialize('anuga.yaml')  # See #1
# model.update()
# model.finalize()
