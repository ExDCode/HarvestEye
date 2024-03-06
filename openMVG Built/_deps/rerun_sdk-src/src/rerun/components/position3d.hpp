// DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/re_types/definitions/rerun/components/position3d.fbs".

#pragma once

#include "../datatypes/vec3d.hpp"
#include "../result.hpp"

#include <array>
#include <cstdint>
#include <memory>

namespace arrow {
    class Array;
    class DataType;
    class FixedSizeListBuilder;
} // namespace arrow

namespace rerun::components {
    /// **Component**: A position in 3D space.
    struct Position3D {
        rerun::datatypes::Vec3D xyz;

      public:
        // Extensions to generated type defined in 'position3d_ext.cpp'

        /// Construct Position3D from x/y/z values.
        Position3D(float x, float y, float z) : xyz{x, y, z} {}

        float x() const {
            return xyz.x();
        }

        float y() const {
            return xyz.y();
        }

        float z() const {
            return xyz.z();
        }

      public:
        Position3D() = default;

        Position3D(rerun::datatypes::Vec3D xyz_) : xyz(xyz_) {}

        Position3D& operator=(rerun::datatypes::Vec3D xyz_) {
            xyz = xyz_;
            return *this;
        }

        Position3D(std::array<float, 3> xyz_) : xyz(xyz_) {}

        Position3D& operator=(std::array<float, 3> xyz_) {
            xyz = xyz_;
            return *this;
        }

        /// Cast to the underlying Vec3D datatype
        operator rerun::datatypes::Vec3D() const {
            return xyz;
        }
    };
} // namespace rerun::components

namespace rerun {
    template <typename T>
    struct Loggable;

    /// \private
    template <>
    struct Loggable<components::Position3D> {
        static constexpr const char Name[] = "rerun.components.Position3D";

        /// Returns the arrow data type this type corresponds to.
        static const std::shared_ptr<arrow::DataType>& arrow_datatype();

        /// Fills an arrow array builder with an array of this type.
        static rerun::Error fill_arrow_array_builder(
            arrow::FixedSizeListBuilder* builder, const components::Position3D* elements,
            size_t num_elements
        );

        /// Serializes an array of `rerun::components::Position3D` into an arrow array.
        static Result<std::shared_ptr<arrow::Array>> to_arrow(
            const components::Position3D* instances, size_t num_instances
        );
    };
} // namespace rerun